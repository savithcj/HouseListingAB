from rest_framework import serializers
from global_listing.models import *


#User profile Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

#Property Serializer
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

#Property Image Serializer
class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=PropertyImages
        fields = '__all__'

#Room space serializer
class RoomSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model=RoomSpace
        fields = '__all__'

#Property address serializer
class PropertyAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAddress
        fields = '__all__'