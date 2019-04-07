from django.urls import path
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatternsOriginal = [
    path('', IndexView.as_view(), name = 'home'),
    path('my_listings/', MyListingsView.as_view(), name='my-listings'),
    path('<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),
    path('post/', ListingCreateView.as_view(), name = 'listing-create'),
    path('<int:pk>/edit/', ListingEditView.as_view(), name='listing-edit'),
]

#API urls:
from rest_framework import routers
from .api import *


router = routers.DefaultRouter()
router.register('api/userprofile', UserProfileViewSet, 'userprofile')
router.register('api/property', PropertyViewSet, 'property')
router.register('api/propertyimage', PropertyImageViewSet, 'propertyimage')
router.register('api/roomspace', RoomSpaceViewSet, 'roomspace')
router.register('api/propertyaddress', PropertyAddressViewSet, 'propertyaddress')

urlpatternsAPI = router.urls


urlpatterns = urlpatternsOriginal + urlpatternsAPI

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)