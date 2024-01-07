from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change_password/', views.set_password, name='change_password'),
    path('change_password_2/', views.set_password2, name='change_password_2'),
    path('', views.profile, name='profile'),

]
