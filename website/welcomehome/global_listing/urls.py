from django.urls import path
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', IndexView.as_view(), name = 'global_listing'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('post/', post, name = 'post'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
