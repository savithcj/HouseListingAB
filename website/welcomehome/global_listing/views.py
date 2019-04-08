from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import *
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.template import loader
from django.urls import reverse
from django.db.models import Q
from django.db import transaction
from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages

from itertools import chain

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
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST, instance=request.user.user_profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.user_profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'registration/profile.html', context)

class IndexView(generic.ListView):
    model = Property
    context_object_name = 'post_list'
    template_name = 'global_listing/index.html'
    ordering = ['-list_date']
    paginate_by = 5
    
    def get_queryset(self):
        qs1 = Property.objects.filter(Q(is_active=True) & Q(post_priority=0)).order_by('-list_date')
        qs2 = Property.objects.filter(Q(is_active=True) & (Q(post_priority=1) | Q(post_priority=2))).order_by('-list_date')
        return list(chain(qs1,qs2))

    # ---------Removed to add pagination----------

    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     context["featured_posts"] = Property.objects.filter(Q(is_active=True) & Q(post_priority=0))
    #     context["recent_posts"] = Property.objects.filter(Q(is_active=True) & (Q(post_priority=1) | Q(post_priority=2))).order_by('-list_date')[:10]
    #     return context

class ListingDetailView(generic.DetailView):
    model = Property
    template_name = "global_listing/listing_detail.html"

class MyListingsView(generic.ListView):
    model = Property
    template_name = 'global_listing/my-listings.html'
    ordering = ['-list_date']
    
    def get_context_data(self, **kwargs):
        context = super(MyListingsView, self).get_context_data(**kwargs)
        context["active_posts"] = Property.objects.filter(Q(is_active=True) & Q(user=self.request.user.user_profile))
        context["inactive_posts"] = Property.objects.filter(Q(is_active=False) & Q(user=self.request.user.user_profile))
        return context

class ListingCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'global_listing/property_form.html'
    model = Property
    form_class = PostForm
    success_url = None

    def get_context_data(self, **kwargs):
        context = super(ListingCreateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context['address_form'] = AddressFormSet(self.request.POST, instance=self.object, prefix='address')
            context['room_form'] = RoomSpaceFormSet(self.request.POST, instance=self.object, prefix='rooms')
            context['image_form'] = ImageFormSet(self.request.POST, self.request.FILES, instance=self.object, prefix='images')
        else:
            context['address_form'] = AddressFormSet(instance=self.object, prefix='address')
            context['room_form'] = RoomSpaceFormSet(instance=self.object, prefix='rooms')
            context['image_form']= ImageFormSet(instance=self.object, prefix='images')
        return context

    def post(self, request, *args, **kwargs):
        """Check if form is valid, and then calls form_valid to check room_forms"""
        form = self.get_form()
        
        if form.is_valid(): # if form is valid, save before proceeding next to check on formsets
            self.object = form.save()
            address_form = self.get_context_data()['address_form']
            room_form = self.get_context_data()['room_form']
            image_form = self.get_context_data()['image_form']
            if address_form.is_valid() and room_form.is_valid() and image_form.is_valid():
                return self.form_valid(form, address_form, room_form, image_form)
            else:
                self.object.delete()
                self.object = None
                return self.form_invalid(form, address_form, room_form, image_form)
        else:
            return self.form_invalid(form, None, None, None)

    def form_invalid(self, form, address_form, room_form, image_form):
        # print(form.errors,room_form.errors)
        return super(ListingCreateView, self).form_invalid(form)

    def form_valid(self, form, address_form, room_form, image_form):
        """Called on if form is valid, saves room_form."""
        self.object.created_by = self.request.user
        self.object.updated_by = self.request.user
        self.object.save()
        address_form.save()
        room_form.save()
        image_form.save()
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

    def get(self, request, *args, **kwargs):
        """Check active status of the listing, ensures that inactive listings cannot be edited."""
        obj = self.get_object()
        if obj.is_active == False:
            return redirect('home')
        else:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ListingEditView, self).get_context_data(**kwargs)
        instance = self.get_object()

        if self.request.POST:   # form being posted by user, POST
            context['address_form'] = AddressFormSet(self.request.POST, instance=instance, prefix='address')
            context['room_form'] = RoomSpaceFormSet(self.request.POST, instance=instance, prefix='rooms')
            context['image_form'] = ImageFormSet(self.request.POST, self.request.FILES, instance=instance, prefix='images')
        
        else:   # form being requested by user, GET
            context['address_form'] = AddressFormSet(instance=instance, prefix='address')
            context['room_form'] = RoomSpaceFormSet(instance=instance, prefix='rooms')
            context['image_form']= ImageFormSet(instance=instance, prefix='images')

            if instance.has_rooms(): # Set extra inline formset to zero if the Property already has rooms
                context['room_form'].extra = 0

        return context

    def post(self, request, *args, **kwargs):
        """Check if form is valid, and then calls form_valid to check room_forms"""
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid(): # if form is valid, save before proceeding next to check on room_forms
            self.object = form.save()
            address_form = self.get_context_data()['address_form']
            room_form = self.get_context_data()['room_form']
            image_form = self.get_context_data()['image_form']
            if address_form.is_valid() and room_form.is_valid() and image_form.is_valid():
                return self.form_valid(form, address_form, room_form, image_form)
            else:
                return self.form_invalid(form, address_form, room_form, image_form)
        else:
            return self.form_invalid(form, None, None, None)

    def form_invalid(self, form, address_form, room_form, image_form):
        # print(form.errors,room_form.errors)
        return super(ListingEditView, self).form_invalid(form)

    def form_valid(self, form, address_form, room_form, image_form):
        """Called on if form is valid, saves room_form."""
        self.object.updated_by = self.request.user
        self.object.save()
        address_form.save()
        room_form.save()
        image_form.save()
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