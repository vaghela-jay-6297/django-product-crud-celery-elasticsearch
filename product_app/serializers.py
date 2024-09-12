# product_app/serializers.py
from rest_framework import serializers
from .models import Product, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image')


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'size', 'color', 'capacity', 'quantity', 'images')

    def create(self, validated_data):
        images_data = self.context.get('request').FILES.getlist('images')  # Retrieve images from request.FILES
        product = Product.objects.create(**validated_data)
        for image_data in images_data:
            Image.objects.create(product=product, image=image_data)
    
        return product

    def update(self, instance, validated_data):
        images_data = self.context.get('request').FILES.getlist('images')
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.size = validated_data.get('size', instance.size)
        instance.color = validated_data.get('color', instance.color)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        
        # Update images
        if images_data:
            instance.images.all().delete()
            for image_data in images_data:
                Image.objects.create(product=instance, image=image_data)
        
        return instance