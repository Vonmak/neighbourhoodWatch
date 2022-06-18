from django.urls import path
from .views import *

urlpatterns=[
    path('',index),
    path('home/',home),
    path('logs/',admin_log),
    path('member/',member),
    path('hood/<id>',hood),
    path('biz/<name>',biz),
    path('login/',login_user),
    path('logout',logout_user),
    # path('<id>/post/',post, name='post'),
]