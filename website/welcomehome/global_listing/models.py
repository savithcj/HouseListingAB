from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# https://docs.djangoproject.com/en/2.1/topics/db/models/
# https://docs.djangoproject.com/en/2.1/ref/models/fields/#model-field-types

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
	email = models.CharField(max_length=30)
	phone_day = PhoneNumberField()
	phone_alt = PhoneNumberField(null=True, blank=True)

class Property(models.Model):
	property_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(UserProfile, related_name='property_user', on_delete=models.DO_NOTHING)
	is_active = models.BooleanField(default=True)
	price = models.PositiveIntegerField(null=True)
	list_date = models.DateField(auto_now=False, auto_now_add=True)
	above_grade_sqft = models.PositiveIntegerField(null=True)
	lot_size = models.PositiveIntegerField(null=True)
	post_title = models.CharField(max_length=128, null=True)
	post_priority = models.IntegerField(default=1)	# 0: featured, > 0: regular priority
	description = models.CharField(max_length=2450)
	is_commercial = models.BooleanField(null=True)
	business = models.CharField(max_length=30,null=True)
	num_of_buildings = models.PositiveIntegerField(null=True)
	is_residential = models.BooleanField(null=True)
	residence_type = models.CharField(max_length=30, null=True)

	def __str__(self):
		return str(self.property_id)

	def save(self, *args, **kwargs):
		if self.post_title is None:
			self.post_title = PropertyAddress.objects.get(property_id=self.property_id)
		super(Property, self).save(*args, **kwargs)

	def address(self):
		return PropertyAddress.objects.get(property_id=self.property_id)

	def image_paths(self):
		images = PropertyImages.objects.filter(property_id=self.property_id)
		return images

	

class RoomSpace(models.Model):
	property_id = models.ForeignKey(Property, related_name='roomspace_property_id', on_delete=models.DO_NOTHING)
	room_id = models.PositiveIntegerField()
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=30)
	ceiling_heights = models.FloatField()
	is_insulated = models.BooleanField()
	num_of_windows = models.PositiveIntegerField()
	fireplace = models.BooleanField()
	size = models.FloatField()

class RoomType(models.Model):
	property_id = models.ForeignKey(RoomSpace, related_name='roomtype_property_id', on_delete=models.DO_NOTHING)
	room_id = models.ForeignKey(RoomSpace, related_name='roomtype_room_id', on_delete=models.DO_NOTHING)
	room_type = models.CharField(max_length=30)

class RoomDimension(models.Model):
	property_id = models.ForeignKey(RoomSpace, related_name='roomdimension_property_id', on_delete=models.DO_NOTHING)
	room_id = models.ForeignKey(RoomSpace, related_name='roomdimension_room_id', on_delete=models.DO_NOTHING)
	dimension = models.FloatField()

class RoomFlooring(models.Model):
	property_id = models.ForeignKey(RoomSpace, related_name='roomfloor_property_id', on_delete=models.DO_NOTHING)
	room_id = models.ForeignKey(RoomSpace, related_name='roomfloor_room_id', on_delete=models.DO_NOTHING)
	flooring = models.CharField(max_length=30)

class PropertyAddress(models.Model):
	property_id = models.ForeignKey(Property, related_name='propertyaddress_property_id', on_delete=models.DO_NOTHING)
	street = models.CharField(max_length = 200)
	city = models.CharField(max_length = 200)
	province = models.CharField(max_length=25)
	postal = models.CharField(max_length = 7)

	def __str__(self):
		return str(self.street)



######### Image Upload

# https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django
# https://www.geeksforgeeks.org/python-uploading-images-in-django/
def get_image_filename(self, instance):
	title = instance.property_id.__str__ + instance.property_id.address
	slug = slugify(title)
	return f"property_images/{slug}"

class PropertyImages(models.Model):
	property_id = models.ForeignKey(Property, related_name='propertyimages_property_id', default=None, on_delete=models.DO_NOTHING)
	image = models.ImageField(upload_to='img_upload/%Y/%m/%D/', verbose_name='Image')

	def image_path(self):
		return get_image_filename

