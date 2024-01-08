from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('logout/', views.user_logout, name='user_logout'),
]