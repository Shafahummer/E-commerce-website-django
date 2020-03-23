
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('register/', views.register),
    path('home/', views.home),
    path('register/index/', views.index),
]
