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

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import Http404

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            p = user.user_profile
            p.email = form.cleaned_data.get('email')
            p.phone_day = form.cleaned_data.get('phone_day')
            p.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class IndexView(generic.ListView):
    model = Property
    context_object_name = 'latest_post_list'
    template_name = 'global_listing/index.html'
    ordering = ['-list_date']
    
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
    
# TODO: User profile and listing view

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
        """Check if form is valid, and then calls form_valid to check room_forms"""
        form = self.get_form()
        
        if form.is_valid(): # if form is valid, save before proceeding next to check on room_forms
            self.object = form.save()
            room_form = self.get_context_data()['room_form']
            if room_form.is_valid():
                return self.form_valid(form, room_form)
            else:
                self.object.delete()
                self.object = None
                return self.form_invalid(form, room_form)
        else:
            return self.form_invalid(form, None)

    def form_invalid(self, form, room_form):
        print(form.errors,room_form.errors)
        return super(ListingCreateView, self).form_invalid(form)

    def form_valid(self, form, room_form):
        """Called on if form is valid, saves room_form."""
        self.object.created_by = self.request.user
        self.object.updated_by = self.request.user
        self.object.save()
        room_form.save()
        return super(ListingCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('listing-detail', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        current_kwargs = super(ListingCreateView, self).get_form_kwargs()
        current_kwargs['user_instance'] = self.request.user
        return current_kwargs


class ListingEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'global_listing/property_form.html'
    model = Property
    form_class = PostForm
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super(ListingEditView, self).get_context_data(**kwargs)

        if self.request.POST:   # form being posted by user
            context['room_form'] = RoomSpaceFormSet(self.request.POST, instance=self.get_object())
        else:   # form being requested by user
            context['room_form'] = RoomSpaceFormSet(instance=self.get_object())
        
        return context

    def post(self, request, *args, **kwargs):
        """Check if form is valid, and then calls form_valid to check room_forms"""
        self.object = self.get_object()
        form = self.get_form()
        
        if form.is_valid(): # if form is valid, save before proceeding next to check on room_forms
            self.object = form.save()
            room_form = self.get_context_data()['room_form']
            if room_form.is_valid():
                return self.form_valid(form, room_form)
            else:
                return self.form_invalid(form, room_form)
        else:
            return self.form_invalid(form, None)

    def form_invalid(self, form, room_form):
        print(form.errors,room_form.errors)
        return super(ListingEditView, self).form_invalid(form)

    def form_valid(self, form, room_form):
        """Called on if form is valid, saves room_form."""
        self.object.updated_by = self.request.user
        self.object.save()
        room_form.save()
        return super(ListingEditView, self).form_valid(form)

    def get_success_url(self):
        return reverse('listing-detail', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        current_kwargs = super(ListingEditView, self).get_form_kwargs()
        current_kwargs['user_instance'] = self.request.user
        return current_kwargs

    def get_object(self, *args, **kwargs):
        """Checks the user id against the owner of the post being edited"""
        obj = super(ListingEditView, self).get_object(*args, **kwargs)
        if obj.user.id != self.request.user.id:
            raise Http404
        return obj