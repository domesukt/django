from django.shortcuts import render

# Create your views here.
from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home')  # URLが呼び出すViewを記述
    
]