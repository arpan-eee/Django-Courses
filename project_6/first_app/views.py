from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    students = models.students.objects.all()
    return render(request, 'home.html',{'students':students})