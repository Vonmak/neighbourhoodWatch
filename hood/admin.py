from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Admin)
admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Post)