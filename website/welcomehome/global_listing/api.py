from rest_framework import viewsets, permissions

from global_listing.models import *

from .serializers import *

#A viewset allows to create a full CRUD API without having to 
#specify explicit methods for functionality
#https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserProfileSerializer

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

class RoomSpaceViewSet(viewsets.ModelViewSet):
    queryset = RoomSpace.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoomSpaceSerializer

class PropertyAddressViewSet(viewsets.ModelViewSet):
    queryset = PropertyAddress.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PropertyAddressSerializer