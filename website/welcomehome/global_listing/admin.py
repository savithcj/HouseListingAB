from django.contrib import admin
from .models import Property, PropertyImages, RoomSpace, UserProfile

# Register your models here.

class PropertyImagesAdmin(admin.StackedInline):
    model = PropertyImages
    
class PropertyRoomsAdmin(admin.StackedInline):
    model = RoomSpace

admin.site.register(UserProfile)

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_id','is_active','price','list_date','user','post_title','post_priority','description','above_grade_sqft','lot_size','is_commercial','business','num_of_buildings','is_residential')
    inlines = [
        PropertyRoomsAdmin,
        PropertyImagesAdmin
    ]

