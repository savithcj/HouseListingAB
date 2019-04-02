from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import PostForm
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.template import loader
from django.urls import reverse
from django.db.models import Q

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
    
    # DetailView generic view uses a template called <app name>/<model name>_detail.html by default, unless overwritten by template_name
    # generic view expects the primary key value captured from the URL to be called 'pk', which is implemented in urls.py


#https://stackoverflow.com/questions/5720287/django-how-to-make-a-form-for-a-models-foreign-keys
#https://stackoverflow.com/questions/10382838/how-to-set-foreignkey-in-createview/10565744#10565744
class ListingCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'global_listing/property_form.html'
    model = Property
    form_class = PostForm

    def form_valid(self, form):
        form.instance.user = self.request.user.user_profile
        return super().form_valid(form)


# # ############### image upload

# def post(request):
#     ImageFormSet = modelformset_factory(PropertyImages, form=ImageForm)

#     if request.method == 'POST':
#         postForm = PostForm(request.POST)
#         formset = ImageFormSet(request.POST, request.FILES, queryset=PropertyImages.objects.none())

#         if postForm.is_valid() and formset.is_valid():
#             post_form = postForm.save(commit=False)
#             post_form.user = request.user
#             post_form.save()

#             for form in formset.cleaned_data:
#                 if form:
#                     image=form['image']
#                     photo=PropertyImages(post=post_form, image=image)
#                     photo.save()
#             messages.success(request,"Upload success!")
#             return HttpResponseRedirect("/")

#         else:
#             print(postForm.errors, formset.errors)
        
#     else:
#         postForm = PostForm()
#         formset = ImageFormSet(queryset=PropertyImages.objects.none())
#     return render(request, 'global_listing/post.html', {'postForm': postForm, 'formset': formset, 'property_instance': instance})
    