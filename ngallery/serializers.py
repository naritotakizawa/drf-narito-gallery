from rest_framework import serializers
from .models import Category, Tag, Product, Image


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'src', 'alt')


class SimpleProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'thumbnail')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    image_set = ImageSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'thumbnail', 'category', 'tags', 'text', 'image_set')
