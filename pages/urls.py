from django.shortcuts import render

# Create your views here.
from django.urls import path
from .views import homePageView, HomePageView

urlpatterns = [
    #URLが呼び出すViewを記述する
    path('kawa', homePageView, name='kawa'), #関数の場合
    path('', HomePageView.as_view(), name='home')   #クラスの場合
]
