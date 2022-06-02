from django.urls import path
from product import views

urlpatterns = [
    path('', views.productlist), # http://127.0.0.1:8000/products/
    path('first/', views.productfirst) # http://127.0.0.1:8000/products/first/  
] 