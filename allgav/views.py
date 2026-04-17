from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from .serializers import ProductListSerializer
from .models import Product

#ListAPIView
#Takes the queryset to return.
#Serializer class to convert the queryset into a serializer.
#The Http method is obviously GET.
# Returns the response object of rest_framework
class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    
    
#RetrieveAPIView
# Returns single record of a table.
# GET method.
class ProductSelectedListView(generics.RetrieveAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "id"

#CreatAPIView
# POST method
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductListSerializer

class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductListSerializer
    lookup_field = 'id' 
    lookup_url_kwarg = 'id'
    queryset = Product.objects.all()

#DestroyAPIView
#POST method.
class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductListSerializer
    lookup_field = "id"
    lookup_url_kwarg = "id"
    queryset = Product.objects.all()

