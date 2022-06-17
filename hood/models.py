from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    pic = CloudinaryField('image')
    house_number = models.IntegerField(default=1)
    phone = models.IntegerField(null=True, blank=True, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admin")
    
    def __str__(self):
        return f'{self.name} Admin'
    
    @receiver(post_save, sender=User)
    def update_user_admin(sender, instance, created, **kwargs):
        if created:
            Admin.objects.create(user=instance)
        instance.admin.save()
    
    def save_admin(self):
        self.save()
        
    def delete_admin(self):
        self.delete()
    
class Neighbourhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    occupants_count = models.IntegerField(default=None)
    admin = models.OneToOneField(Admin, null=True, blank=True, related_name='neighbourhood',on_delete=models.DO_NOTHING)
    def __str__(self):
        return f'{self.name} Neighbourhood'
    
    def save_hood(self):
        self.save()
        
    def delete_hood(self):
        self.delete()
        
    def update_hood(self, new_hood):
        try:
            self.name = new_hood
            self.save()
            return self
        except self.DoesNotExist:
            print('Hood already exists')
            
    def update_count(self, new_count):
        try:
            self.occupants_count = new_count
            self.save()
            return self
        
        except self.DoesNotExist:
            print('Count already exists')

    @classmethod
    def search_by_id(cls, id):
        hood = Neighbourhood.objects.get(id = id)
        return hood
    
    
    
class Business(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    pic = CloudinaryField('image')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='business')
    
    def __str__(self):
        return f'{self.name} Business'
    
    
class Policedept(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    contact = models.IntegerField(null=False, blank=False)
    neighbourhood = models.ForeignKey(Neighbourhood, default=None, on_delete=models.CASCADE, related_name='policedept')
    
    
    def __str__(self):
        return f'{self.name} Policedept'
    
    def save_police(self):
        self.save()
        
    def delete_police(self):
        self.delete()
     
    
    
class Healthdept(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    contact = models.IntegerField(null=False, blank=False)
    neighbourhood = models.ForeignKey(Neighbourhood, default=None, on_delete=models.CASCADE, related_name='healthdept')
    
    def __str__(self):
        return f'{self.name} Healthdept'
    
    def save_health(self):
        self.save()
        
    def delete_health(self):
        self.delete()
     