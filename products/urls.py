from django.urls import path

from .views import CategoryList, CategoryDetail, ProductList, ProductDetail, ProductFeaturedList

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('products/featured/', ProductFeaturedList.as_view(), name='product_featured'),
]