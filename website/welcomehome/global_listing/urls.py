from django.urls import path
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatternsOriginal = [
    path('', IndexView.as_view(), name = 'global_listing'),
    path('<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),
    path('post/', post, name = 'post'),
    
]


#API urls:
from rest_framework import routers
from .api import PropertyViewSet, PropertyImageViewSet

router = routers.DefaultRouter()
router.register('api/property', PropertyViewSet, 'property')
router.register('api/propertyimage', PropertyImageViewSet, 'propertyimage')

urlpatternsAPI = router.urls


urlpatterns = urlpatternsOriginal + urlpatternsAPI

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)