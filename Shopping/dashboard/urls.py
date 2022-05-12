from django.urls import path
from dashboard import views

urlpatterns = [
  path('', views.dashboard_index, name = "dashboard"),
  path('dashboard-products', views.dash_products, name = "dash_products"),
  path('dashboard-categories', views.dash_categories, name = "dash_categories"),
  path('create-category/', views.dash_create_category, name = "dash_create_category"),
  path('create-product/', views.dash_create_product, name = "dash_create_product"),
  path('delete-category/<int:pk>/', views.dash_delete_category, name = "dash_delete_category"),
  path('delete-product/<int:pk>/', views.dash_delete_product, name = "dash_delete_product"),
]