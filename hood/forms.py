from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class UserForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    email=forms.EmailField(max_length=100, required=False)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2','is_admin','is_profile')

class AdminForm(forms.ModelForm):
    class Meta:
        model= Admin
        fields= ['house_number','phone',]
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields= ['house_number','phone',]
   
        
class HoodForm(forms.ModelForm):
    class Meta:
        model= Neighbourhood
        fields= '__all__'
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model= Business
        fields= '__all__'
        
class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=20, widget=forms.PasswordInput)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ['title', 'post']