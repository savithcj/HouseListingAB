from rest_framework import viewsets, permissions

from global_listing.models import *

from .serializers import *

from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

#A viewset allows to create a full CRUD API without having to 
#specify explicit methods for functionality
#https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/

class PropertyAPI(ObjectMultipleModelAPIViewSet):
    querylist = [
        {'queryset': Property.objects.all(), 'serializer_class': PropertySerializer},
        {'queryset': PropertyAddress.objects.all(), 'serializer_class': PropertyAddressSerializer},
        {'queryset': RoomSpace.objects.all(), 'serializer_class': RoomSpaceSerializer}
    ]