from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Service(models.Model):
    stype = models.CharField(max_length=50)

    def __str__(self):
        return self.stype

class Company(models.Model):
    name = models.CharField(max_length=50)
    website_url = models.CharField(max_length=100, null=True, blank=True)
    provided_services = models.ManyToManyField(Service, related_name="provided_services")
    description = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Companies"
    
    def __str__(self):
        return self.name

class CompanyAddress(models.Model):
    company_id = models.OneToOneField(Company, related_name='company_address', on_delete = models.CASCADE)
    street = models.CharField(max_length=200, null=False, blank=False)
    city = models.CharField(max_length=200, null=False, blank=False)
    province = models.CharField(max_length=25, default='AB', null=False, blank=False)
    postal = models.CharField(max_length=7, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return self.company_id.name +": " + self.postal




