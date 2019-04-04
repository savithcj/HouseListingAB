from django.urls import path
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatternsOriginal = [
    path('', IndexView.as_view(), name = 'home'),
    path('<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),
    path('post/', ListingCreateView.as_view(), name = 'listing-create'),
    
]

#API urls:
from rest_framework import routers
from .api import UserProfileViewSet, PropertyViewSet, PropertyImageViewSet, RoomSpaceViewSet, \
    RoomTypeViewSet, RoomDimensionViewSet, RoomFlooringViewSet, PropertyAddressViewSet


router = routers.DefaultRouter()
router.register('api/userprofile', UserProfileViewSet, 'userprofile')
router.register('api/property', PropertyViewSet, 'property')
router.register('api/propertyimage', PropertyImageViewSet, 'propertyimage')
router.register('api/roomspace', RoomSpaceViewSet, 'roomspace')
router.register('api/roomtype', RoomTypeViewSet, 'roomtype')
router.register('api/roomdimension', RoomDimensionViewSet, 'roomdimension')
router.register('api/roomflooring', RoomFlooringViewSet, 'roomflooring')
router.register('api/propertyaddress', PropertyAddressViewSet, 'propertyaddress')

urlpatternsAPI = router.urls


urlpatterns = urlpatternsOriginal + urlpatternsAPI

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)