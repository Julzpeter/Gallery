from django.test import TestCase
from .models import Location,Category,Image

# Create your tests here.
class ImageTestClass(TestCase):
    #set up method
    def setUp(self):
        self.new_category =Category(category_name='Travel')
        self.new_category.save_category()
        self.new_location = Location(location_name='Nakuru')
        self.new_location.save_location()
        # self.new_image = Image(id=1,image_name='flamingo',image_description='Animals',image_path='media/mygallery/')
        


