from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class UserForm(forms.ModelForm):
    email=forms.EmailField(max_length=100, required=False)
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password','is_admin','is_profile')

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
