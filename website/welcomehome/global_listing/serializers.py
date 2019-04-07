from rest_framework import serializers
from global_listing.models import *

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class RoomSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model=RoomSpace
        fields = '__all__'

class PropertyAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAddress
        fields = '__all__'