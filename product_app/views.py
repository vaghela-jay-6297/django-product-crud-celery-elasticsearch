from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from product_app.models import Product
from product_app.serializers import ProductSerializer
from product_app.documents import ProductDocument
from elasticsearch_dsl import Q
from product_app.tasks import add_product_to_elasticsearch, update_product_in_elasticsearch, delete_product_from_elasticsearch

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        instance = serializer.save()    # save & create row into DB
        add_product_to_elasticsearch.delay(instance.id) # async fun calling of tasks.py file to save document

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data) # get data from user
        if serializer.is_valid():   # check serializer validation
            self.perform_create(serializer) # calling above fun
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        instance = serializer.save()    # update & save record into DB
        update_product_in_elasticsearch.delay(instance.id)  # async fun calling of tasks.py file to update document

    def perform_destroy(self, instance):
        delete_product_from_elasticsearch.delay(instance.id)    # async fun calling of tasks.py file to delete document 
        instance.delete()   # delete record of DB


class ProductSearchView(APIView):
    def get(self, request):
        query = request.GET.get('q', None)    # get query parameter from url/user 
        # check if user not provide query/word then give message as response
        if not query:
            return Response({"message": "No query provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        fields = ['size', 'name', 'description', 'color']   # search query/token/term in this field
        q = Q("multi_match", query=query, fields=fields)    # create Q query to find multiple token in given field   
        search = ProductDocument.search().query(q)  # search in given document
        response = search.execute()     # execute query & get response and store into response variable
        # create list dict comprehension
        results = [{    
                        'name': hit.name,
                        'description': hit.description,
                        'size': hit.size,
                        'color': hit.color,
                        'capacity': hit.capacity
                    }
                    for hit in response # get all hits then get all data values from hits & convert into dict list
                ]
        if not results: # if result is null/empty list then give message
            return Response({'message': 'No results found'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result":results}) 
