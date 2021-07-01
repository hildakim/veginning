from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('food/', product, name="product"),
    path('cosmetics/', cosmetics, name="cosmetics"),
    path('cosmetics/<str:id>', cosmeticssub, name="cosmeticssub"),
    path('household/', household, name="household"),
    path('household/<str:id>', householdsub, name="householdsub"),
    path('food/<str:id>', productsub, name="productsub"),
    path('productnew/', productnew, name="productnew"),
    path('productedit/<str:id>', productedit, name="productedit"),
    path('productdelete/<str:id>', productdelete, name="productdelete"),
]