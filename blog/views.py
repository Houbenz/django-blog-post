from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        "title":"post blog 1",
        "author":"hocine benzagouta",
        "create_date":"19-01-2021",
        "content":"there's some content here",
    } ,
    
    {
        "title":"post blog2",
        "author":"John Doe",
        "create_date":"20-01-2021",
        "content":"this is a second post",
    }

]

def home(request):
    context = {
        "posts":posts,
        "title":"fire",
    }
    #put the request and the template path and the context inside the render method, not inside HttpResponse,
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})