from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterform

def register(request):
    if request.method == 'POST':
      form = UserRegisterform(request.POST)
      if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password= form.cleaned_data.get('password')
        messages.success(request,f'Account created for {username} !, now you can log in')    
        return redirect('login')
    else:    
      form = UserRegisterform()
    return render(request,'users/register.html',{'form' : form})

@login_required()
def profile(request):
  return render(request,'users/profile.html')