from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'index.html')

def admin_log(request):
    user_form=UserForm
    admin_form=AdminForm
    if request.method=='POST':
        user_form=UserForm(request.POST, request.FILES)
        admin_form=AdminForm(request.POST, request.FILES)
        if user_form.is_valid() and admin_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            
            user.refresh_from_db()
            user.admin.phone = admin_form.cleaned_data.get('phone')
            user.admin.house_number = admin_form.cleaned_data.get('house_number')
            user.admin.save()
            return HttpResponse('success') 
    else:
        user_form=UserForm()
        admin_form=AdminForm()
    return render(request, 'admin.html',locals())

def member(request):
    user_form=UserForm
    profile_form=ProfileForm
    if request.method=='POST':
        user_form=UserForm(request.POST, request.FILES)
        profile_form=ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            
            user.refresh_from_db()
            user.profile.phone = profile_form.cleaned_data.get('phone')
            user.profile.house_number = profile_form.cleaned_data.get('house_number')
            user.profile.save()
            return HttpResponse('success') 
    else:
        user_form=UserForm()
        profile_form=ProfileForm()
    return render(request, 'profile.html',locals())
        

def hood(request):
    form= HoodForm
    if request.method == 'POST':
        form= HoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
        else:
            form=HoodForm()
    return render(request, 'hood.html', locals())

def login_user(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect(index)
            else:
                return HttpResponse('Such a user does not exist')
        else:
            return HttpResponse("Form is not Valid")
    
    return render(request,'login.html',locals())