from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from global_listing import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('global_listing.urls')),
    path('', include('frontend.urls')),
    path('global_listing/', include('global_listing.urls'), name='global_listing'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('services/', include('services.urls')),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('tips/', TemplateView.as_view(template_name='tips.html'), name='tips'),
    path('api-info/', TemplateView.as_view(template_name='api.html'), name='api-info'),
]