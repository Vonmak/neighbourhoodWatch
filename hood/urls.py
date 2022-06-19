from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',index),
    path('home/',home),
    path('logs/',admin_log),
    path('member/',member),
    path('hood/<id>',hood),
    path('login/',login_user),
    path('logout',logout_user),
    path('profile/<id>',memberprof, name='profile'),
    path('adminprofile/<id>',adminprof, name='admin'),
]