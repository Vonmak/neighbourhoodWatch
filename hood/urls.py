#all imports from views.py
from .views import post
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",post, name="post")
]