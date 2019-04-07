from django.contrib import admin
from .models import *

admin.site.register(Service)

class CompanyAdressAdmin(admin.TabularInline):
    model = CompanyAddress

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website_url', 'description')
    filter_horizontal = ('provided_services',)
    inlines = [
        CompanyAdressAdmin,
    ]

