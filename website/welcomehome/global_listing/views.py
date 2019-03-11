from django.shortcuts import render
from django.views import generic
from .models import *
from django.template import loader
from django.urls import reverse

class IndexView(generic.ListView):
    model = Property
    context_object_name = 'latest_post_list'
    template_name = 'global_listing/index.html'
    
    # ListView uses a template called <app name>/<model name>_list.html by default, unless overwrite by template_name.
    # For generic ListView, the automatically generated context variable is question_list, unless overwriten by context_object_name

    def get_queryset(self):
        return Property.objects.order_by('-list_date')[:10]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["featured_posts"] = Property.objects.filter(post_priority=0)
        context["recent_posts"] = Property.objects.order_by('-list_date')[:10]
        return context

class DetailView(generic.DetailView):
    model = Property
    template_name = "global_listing/detail.html"
    
    # DetailView generic view uses a template called <app name>/<model name>_detail.html by default, unless overwritten by template_name
    # generic view expects the primary key value captured from the URL to be called 'pk', which is implemented in urls.py

