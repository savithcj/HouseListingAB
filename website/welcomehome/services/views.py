from django.shortcuts import render
from .models import Company
from django.views import generic

class IndexServiceView(generic.ListView):
    model = Company
    context_object_name = 'companies'
    template_name = 'services/services.html'
    ordering = ['-provided_services']
    
    def get_queryset(self):
        return Company.objects.all()