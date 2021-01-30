from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterform(UserCreationForm):
    email = forms.EmailField()
    #for styling
    #email = forms.EmailField(widget=forms.TextInput(attrs={'class':'btn btn-primary','value':'hello world'}))
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']