from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'index.html',locals())

def home(request):
    hoods=Neighbourhood.objects.all()
    posts= Post.objects.all()
    business=Business.objects.all()
    profiles=User.objects.all()
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
    form=UserForm
    if request.method=='POST':
        form=UserForm(request.POST, request.FILES)
        # ad_form=AdminForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user.refresh_from_db()
            user.admin.email = form.cleaned_data.get('email')
            user.admin.save()
            return redirect(home)
    else:
        user_form=UserForm()
    return render(request, 'admin.html',locals())

def member(request):
    user_form=UserForm
    if request.method=='POST':
        user_form=UserForm(request.POST, request.FILES)
        # form=ProfileForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save(commit=False)  
            user.save()   
            user.refresh_from_db()
            user.profile.email = user_form.cleaned_data.get('email')
            user.profile.save()
            user_form.save()
            return redirect(home)
    else:
        user_form=UserForm()
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
    b_form= BusinessForm()
    form = PostForm()
    if request.method=='POST':
        if 'upload' in request.POST:
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                h = form.save(commit=False)
                h.user = request.user
                h.hood = hood
                h.save()
            b_form= BusinessForm()   
        elif 'post' in request.POST:
            b_form = BusinessForm(request.POST, request.FILES)
            if b_form.is_valid():
                b = b_form.save(commit=False)
                b.user = request.user
                b.hood = hood
                b.save()
            form = PostForm()
    return render(request, 'hood.html', locals())

def memberprof(request, id):  
    user=User.objects.filter(id=id).first()
    profile = Profile.objects.get(user=id)
    posts = Post.filter_by_user(user.id).order_by('-date')
    bizs = Business.filter_by_user(user.id).order_by('-date')
    current_user = request.user
    if request.method == 'POST':
        pro_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if pro_form.is_valid():
            profile =pro_form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect(index)
    else:
        pro_form=ProfileForm()
        
    return render(request,"profile/memberprof.html",locals())

def adminprof(request, id):  
    user=User.objects.filter(id=id).first()
    admin = Admin.objects.get(user=id)
    posts = Post.filter_by_user(user.id).order_by('-date')
    bizs = Business.filter_by_user(user.id).order_by('-date')
    current_user = request.user
    if request.method == 'POST':
        ad_form = AdminForm(request.POST, request.FILES, instance=request.user.admin)
        if ad_form.is_valid():
            admin =ad_form.save(commit=False)
            admin.user = current_user
            admin.save()
            return redirect(index)
    else:
        ad_form= AdminForm()
        
    return render(request,"profile/adminprof.html",locals())
