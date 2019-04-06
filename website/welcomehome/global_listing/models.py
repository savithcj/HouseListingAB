from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='user_profile', on_delete=models.DO_NOTHING)
	phone_day = PhoneNumberField(null=True, blank=True)
	phone_alt = PhoneNumberField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)
	instance.user_profile.save()


class Property(models.Model):
	user = models.ForeignKey(UserProfile, related_name='property_user', on_delete=models.DO_NOTHING,blank=True)
	is_active = models.BooleanField(default=True, null=False, blank=True)
	price = models.PositiveIntegerField(null=False, blank=False)
	list_date = models.DateField(auto_now=False, auto_now_add=True)
	above_grade_sqft = models.PositiveIntegerField(null=True, blank=True)
	lot_size = models.PositiveIntegerField(null=True, blank=True)
	post_title = models.CharField(max_length=128, null=True)
	post_priority = models.IntegerField(default=1, blank=True)	# 0: featured, > 0: regular priority
	description = models.CharField(max_length=2450, null=True, blank=True)
	is_commercial = models.NullBooleanField(null=True, blank=True)
	business = models.CharField(max_length=30, null=True, blank=True)
	num_of_buildings = models.PositiveIntegerField(null=True, blank=True)
	is_residential = models.NullBooleanField(null=True, blank=True)
	residence_type = models.CharField(max_length=30, null=True, blank=True)

	def __str__(self):
		return str(self.id) 

	def save(self, *args, **kwargs):
		if self.post_title is None:
			self.post_title = PropertyAddress.objects.get(id=self.id)
		super(Property, self).save(*args, **kwargs)

	def image_paths(self):
		# TODO: filter for active postings only
		images = self.property_image.all()
		return images

	# TODO: implement method to return contact information: email, phone number

	

class RoomSpace(models.Model):
	property_id = models.ForeignKey(Property, related_name='room_space', on_delete=models.CASCADE)
	name = models.CharField(max_length=30, null=True, blank=True)
	description = models.CharField(max_length=30, null=True, blank=True)
	floor_level = models.FloatField(default=1, null=True, blank=True) # 0-basement, 1-first floor, 2-second floor, etc
	ceiling_heights = models.FloatField(null=True, blank=True)
	is_insulated = models.BooleanField(null=True, blank=True)
	num_of_windows = models.PositiveIntegerField(null=True, blank=True)
	fireplace = models.BooleanField(null=True, blank=True)
	sqft = models.FloatField(null=True, blank=True)
	dimA = models.FloatField(null=True, blank=True)
	dimB = models.FloatField(null=True, blank=True)
	shape = models.PositiveIntegerField(default=0, null=True, blank=True)	# 0-square/rectangle, 1-round, 2-irregular, 3-other
	flooring = models.PositiveIntegerField(default=0, null=True, blank=True) # 0-carpet, 1-laminate, 2-wood, 3-wood/polymer composite, 4-vinyl, 5-painted concrete, 6-unfinished concrete, 7-other

class PropertyAddress(models.Model):
	property_id = models.OneToOneField(Property, related_name='property_address', on_delete=models.CASCADE)
	street = models.CharField(max_length=200, null=False, blank=False)
	city = models.CharField(max_length=200, null=False, blank=False)
	province = models.CharField(max_length=25, default='AB', null=False, blank=False)
	postal = models.CharField(max_length=7, null=True, blank=True)
	intercom = models.PositiveIntegerField(null=True, blank=True)
	tel = PhoneNumberField(null=True, blank=True)

	def __str__(self):
		return str(self.street)+", "+str(self.postal)

def get_image_filename(instance, filename):
	title = str(instance.id) + datetime.now().strftime("-%Y-%m-%d-%H-%M-%S")
	slug = slugify(title)
	return f"{str(instance.id)}/{slug}"

class PropertyImages(models.Model):
	property_id = models.ForeignKey(Property, related_name='property_image', on_delete=models.CASCADE)
	title = models.CharField(max_length=25, null=True, blank=True)
	image = models.ImageField(upload_to=get_image_filename, verbose_name='Image', null=False, blank=False)

	def image_path(self):
		return get_image_filename