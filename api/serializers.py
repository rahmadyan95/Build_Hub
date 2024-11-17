from rest_framework import serializers
from .models import Product  # Mengimpor model Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  # Menggunakan model Product
        fields = ['id', 'photo_url', 'product_name', 'quantity', 'unit_value', 'status', 'price', 'description']  # Kolom yang akan disertakan dalam output JSON
