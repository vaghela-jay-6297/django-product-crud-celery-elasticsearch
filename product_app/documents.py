from dataclasses import field
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Product

@registry.register_document
class ProductDocument(Document):
    # add index related settings
    class Index:      
        # Name of the Elasticsearch index
        name = "products"  
        # See Elasticsearch Indices API reference for available settings 
        settings = {
            "number_of_shards": 1,  # primary shards of elastic search
            "number_of_replicas": 0 # copies of primary shards of elastic search(replicas)
        }

    class Django:
        # The model associated with this Document
        model = Product     
        # The fields of the model you want to be indexed in Elasticsearch
        field = ['name', 'description', 'size', 'color', 'capacity']