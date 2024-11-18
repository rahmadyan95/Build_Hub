# api/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Product
from .serializers import ProductSerializer

class ProductUploadView(APIView):  # Update class name to reflect 'Product'
    def get(self, request, *args, **kwargs):
        """
        Retrieve all products or a single product by ID.
        """
        product_id = kwargs.get('id', None)

        # Jika ID diberikan, ambil data produk berdasarkan ID
        if product_id:
            product = get_object_or_404(Product, id=product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Jika tidak ada ID, ambil semua data produk
        product_list = Product.objects.all()
        serializer = ProductSerializer(product_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        # Ensure we pass both the data and files from the request
        serializer = ProductSerializer(data=request.data)  # Use 'ProductSerializer'
        
        # Check if the serializer is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # If serializer is not valid, return the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        """
        Update an existing product.
        """
        product_id = kwargs.get('id', None)
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        """
        Delete an existing product.
        """
        product_id = kwargs.get('id', None)
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)