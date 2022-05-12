from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list_create_api_view),
    path('categories/<int:pk>', views.category_list_detail_api_view),
    path('products/', views.product_list_create_api_view),
    path('products/<int:pk>', views.product_list_detail_api_view),
]