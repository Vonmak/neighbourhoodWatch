from django.contrib import admin
from .models import Admin,Policedept,Healthdept, Neighbourhood,Business

# Register your models here.
admin.site.register(Admin)
admin.site.register(Policedept)
admin.site.register(Healthdept)
admin.site.register(Neighbourhood)
admin.site.register(Business)