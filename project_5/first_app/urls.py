from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.submit_form, name='form'),
    path('about/', views.about, name='about'),
]
