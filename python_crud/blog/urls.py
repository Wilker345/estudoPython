from django.urls import path
from . import views

#/blog/
urlpatterns = [
    path('posts/', views.index),
]