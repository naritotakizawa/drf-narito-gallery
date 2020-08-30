from django.db.models import Count, Q
from rest_framework import generics, pagination
from .models import Category, Product
from .serializers import CategorySerializer, SimpleProductSerializer, ProductSerializer


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        filter = Q()
        keyword = self.request.query_params.get('keyword', None)
        if keyword:
            filter = Q(product__title__icontains=keyword) | Q(product__text__icontains=keyword)

        return Category.objects.annotate(
            product_count=Count('product', filter=filter)
        )


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 12


class ProductList(generics.ListAPIView):
    queryset = Product.objects.order_by('-created_at')
    serializer_class = SimpleProductSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()

        keyword = self.request.query_params.get('keyword', None)
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword))

        category = int(self.request.query_params.get('category', 0))
        if category:
            queryset = queryset.filter(category=category)

        return queryset


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.select_related('category')
    serializer_class = ProductSerializer
