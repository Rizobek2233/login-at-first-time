from django.urls import path
from rest_framework import serializers
from . import views


urlpatterns = [
    path('food/delete/<int:id>/', views.delete_food, name='delete_food'),
]
