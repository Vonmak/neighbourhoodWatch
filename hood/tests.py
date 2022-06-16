from django.test import TestCase
from .models import *

# Create your tests here.
class AdminTestCase(TestCase):
    def setUp(self):
        self.new_admin = Admin(name='Vic',email='v@gmail.com',pic='images.jpg',house_number='12',phone='079166')
        self.new_admin.save_admin()
        
    def tearDown(self):
        Admin.objects.all().delete()
        
    def test_save_admin(self):
        self.assertTrue(len(Admin.objects.all()) == 1)
        
    def test_delete_admin(self):
        self.new_admin.save_admin()
        self.new_admin.delete_admin()
        self.assertTrue(len(Admin.objects.all()) == 0)    
   
class PolicedeptTestCase(TestCase):
    def setUp(self):
        self.new_admin = Admin(name='Vic',email='v@gmail.com',pic='images.jpg',house_number='12',phone='079166')
        self.new_admin.save_admin()
        
        
        self.new_police = Policedept(name='kasarani',email='kas@gmail.com',contact='999',admin=self.new_admin)
        self.new_police.save_police()
        
    def tearDown(self):
        Policedept.objects.all().delete()
        
    def test_save_police(self):
        self.assertTrue(len(Policedept.objects.all()) == 1)
        
    def test_delete_police(self):
        self.new_police.save_police()
        self.new_police.delete_police()
        self.assertTrue(len(Policedept.objects.all()) == 0)    
   

class HealthdeptTestCase(TestCase):
    def setUp(self):
        self.new_admin = Admin(name='Vic',email='v@gmail.com',pic='images.jpg',house_number='12',phone='079166')
        self.new_admin.save_admin()
        
        
        self.new_health = Healthdept(name='kasaranih',email='kash@gmail.com',contact='123',admin=self.new_admin)
        self.new_health.save_health()
        
    def tearDown(self):
        Healthdept.objects.all().delete()
        
    def test_save_health(self):
        self.assertTrue(len(Healthdept.objects.all()) == 1)
        
    def test_delete_health(self):
        self.new_health.save_health()
        self.new_health.delete_health()
        self.assertTrue(len(Healthdept.objects.all()) == 0)    
   
class NeighbourhoodTestCase(TestCase):
    def setUp(self):
        self.new_admin = Admin(name='Vic',email='v@gmail.com',pic='images.jpg',house_number='12',phone='079166')
        self.new_admin.save_admin()
        
        self.new_police = Policedept(name='kasarani',email='kas@gmail.com',contact='999',admin=self.new_admin)
        self.new_police.save_police()
        
        self.new_health = Healthdept(name='kasaranih',email='kash@gmail.com',contact='123',admin=self.new_admin)
        self.new_health.save_health()
        
        
        self.new_hood = Neighbourhood(name='kasarani',location='kasarani',occupants_count=100,admin=self.new_admin,policedept=self.new_police,healthdept=self.new_health)
        self.new_hood.save_hood()
        
    def tearDown(self):
        Neighbourhood.objects.all().delete()
        
    def test_save_hood(self):
        self.assertTrue(len(Neighbourhood.objects.all()) == 1)
        
    def test_delete_hood(self):
        self.new_hood.save_hood()
        self.new_hood.delete_hood()
        self.assertTrue(len(Neighbourhood.objects.all()) == 0)  
        
    def test_update_hood(self):
        update_test = self.new_hood.update_hood('kahawa')
        self.assertEqual(update_test.name, 'kahawa')
    
    def test_update_count(self):
        update_test = self.new_hood.update_count(200)
        self.assertEqual(update_test.occupants_count, 200)
  
    def test_get_image_by_id(self):
        obtained_hood = Neighbourhood.search_by_id(self.new_hood.id)
        print(obtained_hood.name)

   
