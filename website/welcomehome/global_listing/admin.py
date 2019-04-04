from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(UserProfile)

class PropertyImagesAdmin(admin.StackedInline):
    model = PropertyImages
    
class PropertyRoomsAdmin(admin.TabularInline):
    model = RoomSpace

# class PropertyRoomTypeAdmin(admin.TabularInline):
#     model = RoomType
#     fk_name = 'property_id'

# class PropertyRoomDimensionAdmin(admin.TabularInline):
#     model = RoomDimension
#     fk_name = 'property_id'

# class PropertyRoomFlooringAdmin(admin.TabularInline):
#     model = RoomFlooring
#     fk_name = 'property_id'

class PropertyAddressAdmin(admin.TabularInline):
    model = PropertyAddress

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_id','is_active','price','list_date','user','post_title','post_priority','description','above_grade_sqft','lot_size','is_commercial','business','num_of_buildings','is_residential')
    inlines = [
        PropertyAddressAdmin,
        PropertyImagesAdmin,
        PropertyRoomsAdmin,
        # PropertyRoomTypeAdmin,
        # PropertyRoomDimensionAdmin,
        # PropertyRoomFlooringAdmin
    ]