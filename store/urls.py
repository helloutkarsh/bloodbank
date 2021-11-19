from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path
from django.shortcuts import render
from django.urls.conf import include
from store import views

urlpatterns = [
    path('',views.showStore),
    path('donation/',views.addDonation),
    path('donors/',views.donorRecords),
]

