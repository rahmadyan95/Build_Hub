# api/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product  # Update this to 'Product'
from .serializers import ProductSerializer  # Update the serializer import to 'ProductSerializer'

class ProductUploadView(APIView):  # Update class name to reflect 'Product'
    def get(self, request, *args, **kwargs):
        product_list = Product.objects.all()  # Update query to 'Product'
        serializer = ProductSerializer(product_list, many=True)  # Use 'ProductSerializer' instead
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Ensure we pass both the data and files from the request
        serializer = ProductSerializer(data=request.data)  # Use 'ProductSerializer'
        
        # Check if the serializer is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # If serializer is not valid, return the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
