from rest_framework import serializers
from global_listing.models import Property, PropertyImages

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