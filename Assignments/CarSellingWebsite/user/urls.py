from django.urls import path,include
from . import views

urlpatterns = [
    path('register/', views.register,name='register'),
    path('logout/', views.user_logout,name='logout'),
    path('edit/', views.edit_profile,name='edit'),
    path('', views.profile,name='profile'),
    path('edit/password/', views.pass_change,name='edit_password'),
    path('comment/<int:id>', views.comment,name='comment'),
    path('login/', views.UserLoginView.as_view(),name='login'),
]