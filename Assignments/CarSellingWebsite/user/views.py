from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm
from car.models import Car
from car.forms import CommentForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('register')
    
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form' : register_form, 'top' : 'Create Account','btn' : 'Create Account'})


class UserLoginView(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Successfully Logged In')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top'] = 'Log In'
        context['btn'] = 'Log In'
        return context
    
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('home')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'register.html', {'form' : profile_form, 'top' : 'Edit Profile Data','btn' : 'Save Changes'})

@login_required
def profile(request):
    data = Car.objects.filter(owner=request.user)
    if request.user.first_name :
        display_name = request.user.first_name
    else:
        display_name = request.user.username
    return render(request, 'profile.html',{'data': data,'display_name' : display_name})

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'register.html', {'form' : form, 'top' : 'Edit Password','btn' : 'Save Changes'})

def comment(request,id):
    car = Car.objects.get(pk=id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.car = car
            comment_form.save()
            messages.success(request, 'Comment Added')
            return redirect('home')    
    else:
        comment_form = CommentForm()
    return render(request, 'register.html', {'form' : comment_form, 'top' : 'Add Comment','btn' : 'Comment'})
