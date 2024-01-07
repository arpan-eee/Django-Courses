from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.cleaned_data['author']=request.user
            post_form.instance.author = request.user
            post_form.save()
            return redirect('home')
    else:
        post_form = forms.PostForm()
    return render(request, 'add_post.html',{'form':post_form})

@login_required
def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)

    if request.method == 'POST':
        post_form = forms.PostForm(request.POST,instance=post)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('profile')
    return render(request, 'add_post.html',{'form':post_form})

@login_required
def delete_post(request,id):
    post = models.Post.objects.get(pk=id).delete()
    return redirect('home')