from django.shortcuts import render
from django.views import generic
from .models import PropertyListing

class IndexView(generic.ListView):
    template_name = "global_listing/index.html"
    model = PropertyListing

    def get_queryset(self):
        return PropertyListing.objects

class DetailView(generic.DetailView):
    template_name = "global_listing/detail.html"
    model = PropertyListing


# Create your views here.
