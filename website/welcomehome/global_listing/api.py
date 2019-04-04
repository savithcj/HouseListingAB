from rest_framework import viewsets, permissions

from global_listing.models import UserProfile, Property, PropertyImages, \
    RoomSpace, RoomType, RoomDimension, RoomFlooring, PropertyAddress

from .serializers import UserProfileSerializer, PropertySerializer, \
    PropertyImageSerializer, RoomSpaceSerializer, RoomTypeSerializer, \
    RoomDimensionSerializer, RoomFlooringSerializer, PropertyAddressSerializer

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

class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoomTypeSerializer

class RoomDimensionViewSet(viewsets.ModelViewSet):
    queryset = RoomDimension.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoomDimensionSerializer

class RoomFlooringViewSet(viewsets.ModelViewSet):
    queryset = RoomFlooring.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RoomFlooringSerializer

class PropertyAddressViewSet(viewsets.ModelViewSet):
    queryset = PropertyAddress.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PropertyAddressSerializer