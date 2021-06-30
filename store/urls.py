from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', product, name="product"),
    path('<str:id>', productsub, name="productsub"),
    path('gamenew/', productnew, name="productnew"),
]