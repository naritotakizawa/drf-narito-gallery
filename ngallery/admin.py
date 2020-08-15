from django.contrib import admin
from .models import Category, Tag, Product, Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
