from django.urls import path
from .views import IndexServiceView

urlpatterns = [
    path('', IndexServiceView.as_view(), name = 'services'),
]