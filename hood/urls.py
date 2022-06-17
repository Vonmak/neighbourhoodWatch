from django.urls import path
from .views import *

urlpatterns=[
    path('',index),
    path('logs/',admin_log),
    path('member/',member),
    path('hood/',hood),
    # path('biz/',biz),
    path('login/',login_user),
]