from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from . import models
from . import forms
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

def buy(request, id):
    car = models.Car.objects.get(pk=id)

    if request.method == 'GET':
        car_form = forms.CarForm(request.POST)
        if car_form.is_valid():
            if car.owner == request.user:
                messages.warning(request, "You already own this car")
            else:
                car.owner = request.user
                car.quantity -= 1
                car.save()
            return redirect('home')
    return redirect('home')