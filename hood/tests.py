# from hashlib import new
# from django.test import TestCase
# from .models import *
# from django.contrib.auth.models import User

# # Create your tests here.
# class AdminTestCase(TestCase):
#     def setUp(self):
#         self.new_user = User(username='victor')
#         self.new_user.save()
        
#         self.new_admin = Admin(name='Vic',email='v@gmail.com',pic='images.jpg',house_number='12',phone='079166', user=self.new_user)
#         self.new_admin.save_admin()
        
#     def tearDown(self):
#         Admin.objects.all().delete()
        
#     def test_save_admin(self):
#         self.assertTrue(len(Admin.objects.all()) == 1)
        
#     def test_delete_admin(self):
#         self.new_admin.save_admin()
#         self.new_admin.delete_admin()
#         self.assertTrue(len(Admin.objects.all()) == 0)    
   
# class ProfileTestCase(TestCase):
#     def setUp(self):
#         self.another_user = User(username='james')
#         self.another_user.save()
        
#         self.new_profile = Profile(name='kasarani',email='kas@gmail.com',contact='999',admin=self.another_user)
#         self.new_profile.save_profile()
        
#     def tearDown(self):
#         Profile.objects.all().delete()
        
#     def test_save_profile(self):
#         self.assertTrue(len(Profile.objects.all()) == 1)
        
#     def test_delete_profile(self):
#         self.new_profile.save_profile()
#         self.new_profile.delete_profile()
#         self.assertTrue(len(Profile.objects.all()) == 0)    
     
   
# class NeighbourhoodTestCase(TestCase):
#     def setUp(self):
#         self.new_admin = Admin(name='Vic',email='v@gmail.com',pic='images.jpg',house_number='12',phone='079166')
#         self.new_admin.save_admin()
        
#         self.new_profile = Profile(name='kasarani',email='kas@gmail.com',contact='999',admin=self.new_admin)
#         self.new_profile.save_profile()
        
        
#         self.new_hood = Neighbourhood(name='kasarani',location='kasarani',occupants_count=100,admin=self.new_admin,profiledept=self.new_profile,healthdept=self.new_health)
#         self.new_hood.save_hood()
        
#     def tearDown(self):
#         Neighbourhood.objects.all().delete()
        
#     def test_save_hood(self):
#         self.assertTrue(len(Neighbourhood.objects.all()) == 1)
        
#     def test_delete_hood(self):
#         self.new_hood.save_hood()
#         self.new_hood.delete_hood()
#         self.assertTrue(len(Neighbourhood.objects.all()) == 0)  
        
#     def test_update_hood(self):
#         update_test = self.new_hood.update_hood('kahawa')
#         self.assertEqual(update_test.name, 'kahawa')
    
#     def test_update_count(self):
#         update_test = self.new_hood.update_count(200)
#         self.assertEqual(update_test.occupants_count, 200)
  
#     def test_get_image_by_id(self):
#         obtained_hood = Neighbourhood.search_by_id(self.new_hood.id)
#         print(obtained_hood.name)

   
