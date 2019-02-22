from django.shortcuts import render
from django.views import generic
from .models import Property

class IndexView(generic.ListView):
    template_name = "global_listing/index.html"
    model = Property

    def get_queryset(self):
        return Property.objects

class DetailView(generic.DetailView):
    template_name = "global_listing/detail.html"
    model = Property
