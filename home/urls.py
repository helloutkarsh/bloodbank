from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path
from django.shortcuts import render
from django.urls.conf import include
from home import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('store/', include('store.urls'))
]
