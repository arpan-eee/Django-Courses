from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("this is f/a home page")
def courses(request):
    return HttpResponse("this is f/a courses page")
def about(request):
    return HttpResponse("this is f/a about page")

# Create your views here.
