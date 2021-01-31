from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post




def home(request):
    context = {
        "posts":Post.objects.all(),
    }
    #put the request and the template path and the context inside the render method, not inside HttpResponse,
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model=Post
    #by default in class based views django looks for a template, with naming convention
    #<app>/<model>_<view>
    template_name='blog/home.html'
    context_object_name='posts'
    ordering= ['-create_date']
    paginate_by = 2

class PostDetailView(DetailView):
    model=Post
    #by default in class based views django looks for a template, with naming convention
    #<app>/<model>_<viewtype>

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=["title","content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Post
    fields=["title","content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
            
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model=Post  
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
            
        return False
    


def about(request):
    return render(request,'blog/about.html')

