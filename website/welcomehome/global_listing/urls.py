#------------------------------------------------------------------------------------
#Original urls: uncomment these to revert to original version

# from django.urls import path
# from .views import *
# from django.contrib import admin
# from django.conf import settings
# from django.conf.urls.static import static


# urlpatterns = [
#     path('', IndexView.as_view(), name = 'global_listing'),
#     path('<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),
#     path('post/', post, name = 'post'),
    
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------
#API urls: uncomment these to use API version
from rest_framework import routers
from .api import PropertyViewSet

router = routers.DefaultRouter()
router.register('api/property', PropertyViewSet, 'property')

urlpatterns = router.urls
#------------------------------------------------------------------------------------
