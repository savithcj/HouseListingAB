from rest_framework import serializers
from .models import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyAddress
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'