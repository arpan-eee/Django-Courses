from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login , update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('homepage')
    
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form' : register_form, 'type' : 'Create Account' , 'btn' : 'Create Account'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('homepage')
            else:
                messages.warning(request, 'Login information incorrect')
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form' : form, 'type' : 'Log In' , 'btn' : 'Log In'})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('homepage')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'register.html', {'form' : profile_form , 'type' : 'Change User Info' , 'btn' : 'Save Changes'})

@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')