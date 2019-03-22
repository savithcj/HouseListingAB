from rest_framework import serializers
from global_listing.models import Property

#Property Serializer
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'