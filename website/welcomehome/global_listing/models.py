from django.db import models
from django.template.defaultfilters import slugify

# https://docs.djangoproject.com/en/2.1/topics/db/models/
# https://docs.djangoproject.com/en/2.1/ref/models/fields/#model-field-types


# https://stackoverflow.com/questions/34006994/how-to-upload-multiple-images-to-a-blog-post-in-django
def get_image_filename(self, instance, filename):
	title = instance.post.title
	slug = slugify(title)
	return f"property_images/{slug}-{filename}"

class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	email = models.CharField(max_length=30)

# class PhoneNumber(models.Model):
# 	user_id = models.ForeignKey(User, related_name='user_id', on_delete=models.DO_NOTHING)

class Property(models.Model):
	property_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(User, related_name='property_user_id', on_delete=models.DO_NOTHING)
	is_active = models.BooleanField()
	price = models.PositiveIntegerField()
	list_date = models.DateField(auto_now=False, auto_now_add=True)
	lot_size = models.PositiveIntegerField()
	description = models.CharField(max_length=2000)
	is_commercial = models.BooleanField()
	business = models.CharField(max_length=30)
	num_of_buildings = models.PositiveIntegerField()
	is_residential = models.BooleanField()
	residence_type = models.CharField(max_length=30)

	def __str__(self):
		return self.property_id #TODO: change to return address & price


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

class PropertyImages(models.Model):
	property_id = models.ForeignKey(Property, related_name='propertyimages_property_id', on_delete=models.DO_NOTHING)
	image = models.ImageField(upload_to=get_image_filename, verbose_name='Image')

class PropertyAddress(models.Model):
	property_id = models.ForeignKey(Property, related_name='propertyaddress_property_id', on_delete=models.DO_NOTHING)
	street = models.CharField(max_length = 200)
	city = models.CharField(max_length = 200)
	province = models.CharField(max_length=25)
	postal = models.CharField(max_length = 7)
