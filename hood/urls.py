
#all imports from views.py
from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',index),
    path('logs/',admin_log),
    path('member/',member),
    path('hood/',hood),
    # path('biz/',biz),
    path('login/',login_user),
    # path("",post, name="post"),

]