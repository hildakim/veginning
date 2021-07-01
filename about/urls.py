from django.urls import path
from .views import *

urlpatterns = [
    path('forstarter/', about_view, name="forstarter"),
    path('why/', why_view, name="why"),
    path('more/', more_view, name="more"),
    path('bad/', bad_view, name="bad"),
]