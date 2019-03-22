from global_listing.models import Property, PropertyImages
from rest_framework import viewsets, permissions
from .serializers import PropertySerializer, PropertyImageSerializer

#A viewset allows to create a full CRUD API without having to 
#specify explicit methods for functionality
#https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/

#Property Viewset
class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PropertySerializer

class PropertyImageViewSet(viewsets.ModelViewSet):
    queryset = PropertyImages.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PropertyImageSerializer