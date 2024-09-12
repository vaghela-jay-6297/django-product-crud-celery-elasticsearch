from celery import shared_task
from product_app.models import Product
from product_app.documents import ProductDocument

@shared_task
def add_product_to_elasticsearch(product_id):   # add documents in product index using this fun   
    product = Product.objects.get(id=product_id)    # get product id from product table where id=product_id
    product_doc = ProductDocument(      # create document with passing document data field
        meta={'id': product.id},
        id=product.id,
        name=product.name,
        description=product.description,
        size=product.size,
        color=product.color,
        capacity=product.capacity
    )
    product_doc.save()  # save document in ES

@shared_task
def update_product_in_elasticsearch(product_id):    # update documents in product index using this fun 
    product = Product.objects.get(id=product_id)    # get product id from product table where id=product_id
    product_doc = ProductDocument.get(id=product.id)    # get document object where id=product.id
    product_doc.name = product.name     # update name
    product_doc.description = product.description   # update description
    product_doc.size = product.size     
    product_doc.color = product.color
    product_doc.capacity = product.capacity
    product_doc.save()  # # save changes in document of ES

@shared_task
def delete_product_from_elasticsearch(product_id):      # delete documents in product index using this fun
    product_doc = ProductDocument.get(id=product_id)    # get product id from product table where id=product_id
    product_doc.delete()    # delete document