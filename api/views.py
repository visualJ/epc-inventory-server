from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.models import Product, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
