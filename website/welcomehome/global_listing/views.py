from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.template import loader
from django.urls import reverse
from django.db.models import Q
from django.db import transaction
from django.urls import reverse_lazy


##### imports for image upload
# from django.contrib import messages
# from django.http import HttpResponseRedirect

# from django.forms import modelformset_factory
# from .forms import *


class IndexView(generic.ListView):
    model = Property
    context_object_name = 'latest_post_list'
    template_name = 'global_listing/index.html'
    ordering = ['-list_date']
    
    # ListView uses a template called <app name>/<model name>_list.html by default, unless overwrite by template_name.
    # For generic ListView, the automatically generated context variable is question_list, unless overwriten by context_object_name

    def get_queryset(self):
        return Property.objects.order_by('-list_date')[:10]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["featured_posts"] = Property.objects.filter(post_priority=0)
        context["recent_posts"] = Property.objects.filter(Q(post_priority=1) | Q(post_priority=2)).order_by('-list_date')[:10]
        return context

class ListingDetailView(generic.DetailView):
    model = Property
    template_name = "global_listing/listing_detail.html"
    

class ListingCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'global_listing/property_form.html'
    model = Property
    form_class = PostForm
    success_url = None

    def get_context_data(self, **kwargs):
        context = super(ListingCreateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context['room_form'] = RoomSpaceFormSet(self.request.POST, instance=self.object)
        else:
            context['room_form'] = RoomSpaceFormSet(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        formset = PostForm(request.POST, prefix='property_id')
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        context = self.get_context_data()
        room_form = context['room_form']

        with transaction.atomic():

            form.instance.created_by = self.request.user
            form.instance.updated_by = self.request.user
            self.object = form.save()

            if room_form.is_valid():
                room_form.instance = self.object
                room_form.save()

        return super(ListingCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('listing_detail', kwargs={'pk': self.object.pk})

    # def get(self, request):
    #     form = PostForm()
    #     return render(request, self.template_name, {'form':form})

    # def form_valid(self, form):
    #     form.instance.user = self.request.user.user_profile
    #     return super().form_valid(form)

