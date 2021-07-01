from django.urls import path
from .views import *

urlpatterns = [
    path('free/', free_view, name="free"),
    path('recipe/', recipe_view, name="recipe"),
    path('restaurant/', restaurant_view, name="restaurant"),
]