from django.shortcuts import render
from django.http import HttpResponse
from .models import Post




def home(request):
    context = {
        "posts":Post.objects.all(),
        "title":"fire",
    }
    #put the request and the template path and the context inside the render method, not inside HttpResponse,
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})