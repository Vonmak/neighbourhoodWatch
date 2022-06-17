from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    is_profile = models.BooleanField('Is profile',default=False)
    is_admin = models.BooleanField('Is admin',default=False)
    

class Admin(models.Model):
    email = models.EmailField(max_length=30)
    pic = CloudinaryField('image')
    house_number = models.IntegerField(default=1)
    phone = models.IntegerField(null=True, blank=True, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admin")
    
    def __str__(self):
        return f'{self.user.username} Admin'
    
    @receiver(post_save, sender=User)
    def update_user(sender, instance, created, **kwargs):
        if instance.is_admin:
           Admin.objects.get_or_create(user = instance)
            

    @receiver(post_save, sender=User)
    def save_user(sender, instance, **kwargs):
        if instance.is_admin:
            instance.admin.save()
            
            
    def delete_admin(self):
        self.delete()
    
class Neighbourhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    occupants_count = models.IntegerField(default=None)
    admin = models.OneToOneField(Admin, null=True, blank=True, related_name='neighbourhood',on_delete=models.DO_NOTHING)
    health = models.IntegerField(null=True, blank=True)
    police = models.IntegerField(null=True, blank=True)
    
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
    
    

class Profile(models.Model):
    email = models.EmailField(max_length=30)
    phone = models.IntegerField(null=True, blank=True, unique=True)
    pic = CloudinaryField('image')
    house_number = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    hood = models.ForeignKey(Neighbourhood, null=True, blank=True, related_name='members',on_delete=models.DO_NOTHING)
    
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    @receiver(post_save, sender=User)
    def update_user(sender, instance, created, **kwargs):
        if instance.is_profile:
            Profile.objects.get_or_create(user = instance)


    @receiver(post_save, sender=User)
    def save_user(sender, instance, **kwargs):
        if instance.is_profile:
            instance.profile.save()
     
    def delete_profile(self):
        self.delete()
        