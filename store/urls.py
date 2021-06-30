from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', product, name="product"),
    path('<str:id>', productsub, name="productsub"),
    path('productnew/', productnew, name="productnew"),
    path('productedit/<str:id>', productedit, name="productedit"),
    path('productdelete/<str:id>', productdelete, name="productdelete"),
]