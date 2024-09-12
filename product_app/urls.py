from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from product_app.views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, ProductSearchView

urlpatterns = [
    path('product', ProductListCreateAPIView.as_view(), name='product-list-create'),   # create product & get list
    path('product/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'), # retrieve, update, delete product
    path('search/', ProductSearchView.as_view(), name='product-search'),
]

# here set media folder when user's upload their images like product images
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

