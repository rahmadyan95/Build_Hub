from django.urls import path, include
from .views import ProductUploadView

urlpatterns = [
    path('products/', ProductUploadView.as_view(), name='barang-upload'),
]