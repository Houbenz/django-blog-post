from django.shortcuts import render, redirect
from django.contrib import messages
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

     # messages.warning(request,f'Something wrong')
     #return redirect('register')

    else:    
      form = UserRegisterform()
    return render(request,'users/register.html',{'form' : form})
