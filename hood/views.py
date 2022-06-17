from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def admin_log(request):
    form=AdminForm
    if request.method=='POST':
        form = AdminForm(request.POST, request.FILES)
        if form.is_valid():
            admin=form.save()
            admin.save()
            print(admin)
            return HttpResponse('success') 
    else:
        form=AdminForm()
    return render(request, 'adminpro.html',locals())
        
def admin(request):
    form = RegistrationForm
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user =  form.save()
            user.refresh_from_db()
            user.admin.email = form.cleaned_data.get('email')
            user.save()
            form.save()
        return redirect(index)
    return render(request, 'admin.html',locals())

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