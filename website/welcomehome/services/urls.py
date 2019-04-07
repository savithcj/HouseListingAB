from django.urls import path, include
from .views import IndexServiceView


#API urls:
from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register(r'company', CompanyAPI, base_name = 'company')


urlpatterns = [
    path('', IndexServiceView.as_view(), name = 'services'),
    path('api/', include((router.urls, 'companies'), namespace='companies')),
]