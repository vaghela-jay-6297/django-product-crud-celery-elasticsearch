from django.contrib import admin
from .models import Product, Image

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity')
    search_fields = ('size', 'color', 'capacity')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Product, ProductAdmin)
admin.site.register(Image)