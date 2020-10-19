from rest_framework import serializers
from .models import Category, Product, Image


class CategoryWithProductCountSerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'product_count')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'src', 'alt')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    image_set = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'thumbnail', 'category', 'text', 'image_set', 'created_at',)
