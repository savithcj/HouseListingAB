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
    http_method_names = ['get', 'head']

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PropertySerializer
    http_method_names = ['get', 'head']

class PropertyImageViewSet(viewsets.ModelViewSet):
    queryset = PropertyImages.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PropertyImageSerializer
    http_method_names = ['get', 'head']

class RoomSpaceViewSet(viewsets.ModelViewSet):
    queryset = RoomSpace.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoomSpaceSerializer
    http_method_names = ['get', 'head']

class PropertyAddressViewSet(viewsets.ModelViewSet):
    queryset = PropertyAddress.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PropertyAddressSerializer
    http_method_names = ['get', 'head']