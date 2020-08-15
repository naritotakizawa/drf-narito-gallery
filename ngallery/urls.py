from django.urls import path
from . import views

app_name = 'ngallery'

urlpatterns = [
    path('api/products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('api/products/', views.ProductList.as_view(), name='product_list'),
    path('api/categories/', views.CategoryList.as_view(), name='category_list'),
    path('api/tags/', views.TagList.as_view(), name='tag_list'),
]
