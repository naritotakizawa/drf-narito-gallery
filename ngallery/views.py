from rest_framework import generics
from .models import Category, Tag, Product
from .serializers import CategorySerializer, TagSerializer, SimpleProductSerializer, ProductSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = SimpleProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
