from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    pic = CloudinaryField('image')
    house_number = models.IntegerField(default=None)
    phone = models.IntegerField(null=False, blank=False, unique=True)
    
    def __str__(self):
        return f'{self.name} Admin'
    
    def save_admin(self):
        self.save()
        
    def delete_admin(self):
        self.delete()
     
    

class Policedept(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    contact = models.IntegerField(null=False, blank=False)
    admin = models.ForeignKey(Admin, null=True, blank=True, related_name='policedept',on_delete=models.CASCADE)
    
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
    admin = models.ForeignKey(Admin, null=True, blank=True, related_name='healthdept',on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} Healthdept'
    
    def save_health(self):
        self.save()
        
    def delete_health(self):
        self.delete()
     

class Neighbourhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    occupants_count = models.IntegerField(default=None)
    admin = models.ForeignKey(Admin, null=True, blank=True, related_name='neighbourhood',on_delete=models.CASCADE)
    policedept = models.ForeignKey(Policedept, null=True, blank=True, related_name='neighbourhood',on_delete=models.CASCADE)
    healthdept = models.ForeignKey(Healthdept, null=True, blank=True, related_name='neighbourhood',on_delete=models.CASCADE)
    
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