from django.urls import path, include
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

#API urls:
from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register(r'property', PropertyAPI, base_name = 'property')

urlpatterns = [
    path('', IndexView.as_view(), name = 'home'),
    path('my_listings/', MyListingsView.as_view(), name='my-listings'),
    path('<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),
    path('post/', ListingCreateView.as_view(), name = 'listing-create'),
    path('<int:pk>/edit/', ListingEditView.as_view(), name='listing-edit'),
    path('api/', include((router.urls, 'properties'), namespace='properties')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)