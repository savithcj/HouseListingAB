from rest_framework import serializers
from global_listing.models import UserProfile, Property, PropertyImages, \
    RoomSpace, RoomType, RoomDimension, RoomFlooring, PropertyAddress


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

#Room type serializer
class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

#Room dimension serializer
class RoomDimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomDimension
        fields = '__all__'

#Room flooring serializer
class RoomFlooringSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomFlooring
        fields = '__all__'

#Property address serializer
class PropertyAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAddress
        fields = '__all__'