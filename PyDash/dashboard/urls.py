from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dispenseInfo/', views.dispenseInfo),
    path('salesInfo/', views.salesInfo),
    path('deviceInfo/', views.deviceInfo),
    path('deviceInfo/', views.deviceInfo),
    path('userInfo/', views.userInfo),
    path('rfidInfo/', views.rfidInfo),


]



