
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('register/', views.register),
    path('register/login/', views.login),
    path('register/login/login/', views.login),
    path('login/login/', views.login),

    path('login/', views.login),
    path('logout/', views.logout),

]
