from django.shortcuts import render,redirect
from car.models import Car,Comment
from brand.models import Brand
from django.contrib import messages

def home(request,category_slug = None):
    data = Car.objects.all()
    flag = False
    if category_slug is not None:
        flag = True
        brand = Brand.objects.get(slug = category_slug)
        data = Car.objects.filter(brand = brand)
    brands = Brand.objects.all()
    return render(request, 'home.html', {'data' : data, 'brands' : brands,'flag':flag})

def details(request,id):
    carg = Car.objects.get(pk=id)
    car = Car.objects.filter(pk=id)
    comments = Comment.objects.filter(car = carg)
    return render(request, 'details.html', {'car' : car,'comments' : comments})


