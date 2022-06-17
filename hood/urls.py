from django.urls import path
from .views import *

urlpatterns=[
    path('',index),
    path('logs/',admin_log),
    path('adminreg/',admin),
    path('hood/',hood)
    
]