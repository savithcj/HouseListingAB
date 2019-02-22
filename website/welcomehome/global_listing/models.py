from django.db import models

# https://docs.djangoproject.com/en/2.1/topics/db/models/
# https://docs.djangoproject.com/en/2.1/ref/models/fields/#model-field-types
# https://cloudinary.com/documentation/django_image_and_video_upload

class Property(models.Model):
	property_id = models.AutoField(primary_key=True)
	is_active = models.BooleanField()
	price = models.PositiveIntegerField()
	list_date = models.DateField(auto_now=False, auto_now_add=True)
	lot_size = models.PositiveIntegerField()
	description = models.CharField()


	def __str__(self):
		return self.property_id #TODO: change to return address & price

	
class PropertyImage(models.Model):
	property_id = models.ForeignKey(Property, related_name='images', on_delete=models.DO_NOTHING)
	image = models.ImageField()

class PropertyAddress(models.Model):
	property_id = models.ForeignKey(Property, related_name='address', on_delete=models.DO_NOTHING)
	street = models.CharField(max_length = 200)
	city = models.CharField(max_length = 200)
	province = models.CharField(max_length=25)
	postal = models.CharField(max_length = 7)
