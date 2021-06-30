from django.urls import path
from .views import *

urlpatterns = [
    path('forstarter/', about_view, name="forstarter"),
]