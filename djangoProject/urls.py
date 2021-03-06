"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from app01 import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('indexHtml/', views.indexHtml),
    path('json/', views.json),
    # cbv = class based view ,fbv = function base view
    re_path(r'cbv/json/(\d+)/', views.Jsons.as_view()),
    re_path(r'cbv/json2/(?P<age>\d+)/', views.Jsons2.as_view()),

    # app01开头的指向app01目录下的urls.py , 路由分发
    path('app01/',include('app01.urls'))
]
