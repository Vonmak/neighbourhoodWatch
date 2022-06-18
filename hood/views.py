from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'index.html',locals())

def home(request):
    hoods=Neighbourhood.objects.all()
    print(hoods)
    business=Business.objects.all()
    profiles=Profile.objects.all()
    form= HoodForm
    if request.method == 'POST':
        form= HoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
        else:
            form=HoodForm()
    return render(request, 'home.html',locals())

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
            return HttpResponse(home) 
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
            return redirect(home) 
    else:
        user_form=UserForm()
        profile_form=ProfileForm()
    return render(request, 'profile.html',locals())
    
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
                return redirect(home)
            else:
                return HttpResponse('Such a user does not exist')
        else:
            return HttpResponse("Form is not Valid")
    
    return render(request,'login.html',locals())

        
def logout_user(request):
    logout(request)
    return redirect(home)

def hood(request, id):
    hood = Neighbourhood.objects.get(id=id)
    biz=Business.filter_by_hood(hood.id)
    members=Profile.filter_by_hood(hood.id)
    posts=Post.filter_by_hood(hood.id)
    form = PostForm()
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            h = form.save(commit=False)
            h.user = request.user
            h.hood = hood
            h.save()
            return HttpResponseRedirect(request.path_info)
    return render(request, 'hood.html', locals())

# def biz(request, name):
#     biz = Business.objects.get(name=name)
#     form= BusinessForm
#     if request.method == 'POST':
#         form=BusinessForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(index)
#         else:
#             form=BusinessForm()
#     return render(request, 'biz.html', locals())

