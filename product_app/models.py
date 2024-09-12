from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    capacity = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField()
    # many to many field for mutiple image file 
    images = models.ManyToManyField('Image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return str(self.id) + '-' + self.image.name 