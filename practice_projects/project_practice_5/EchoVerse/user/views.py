from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,SetPasswordForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,"Account Created Successfully")
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()
    return render(request,'register.html',{'form':register_form,'top':'Create Account','btn':'Sign Up'})

def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request,request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request,"Logged In Successfully")
                login(request,user)
                return redirect('profile')
            else:
                messages.warning(request,"Invalid Username or Password")
                return redirect('login')
    else:
        login_form = AuthenticationForm()
    return render(request,'register.html',{'form':login_form,'top':'User Log In','btn':'Log In'})

@login_required
def user_logout(request):
    messages.success(request,"Logged Out Successfully")
    logout(request)
    return redirect('home')

@login_required
def set_password(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Password Has Been Changed")
            update_session_auth_hash(request,form.user)
            return redirect('home')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request,'register.html',{'form':form,'top':'Change Password','btn':'Save Changes'})

@login_required
def set_password2(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Password Has Been Changed")
            update_session_auth_hash(request,form.user)
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'register.html',{'form':form,'top':'Change Password','btn':'Save Changes'})

@login_required
def profile(request):
    return render(request,'profile.html')


    

