from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

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

@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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

@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    # pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

@login_required
def delete_post(request,id):
    post = models.Post.objects.get(pk=id).delete()
    return redirect('home')

@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')