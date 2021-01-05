from django.urls import path, re_path, include
from app01 import views

urlpatterns = [
    # app01/index/
    path('index/', views.index),
]
