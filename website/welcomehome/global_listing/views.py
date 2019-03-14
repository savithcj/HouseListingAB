from django.shortcuts import render
from django.views import generic
from .models import *
from django.template import loader
from django.urls import reverse
from django.db.models import Q

##### imports for image upload
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from .forms import *


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
        context["recent_posts"] = Property.objects.filter(Q(post_priority=1) | Q(post_priority=2)).order_by('-list_date')[:10]
        return context

class DetailView(generic.DetailView):
    model = Property
    template_name = "global_listing/detail.html"
    
    # DetailView generic view uses a template called <app name>/<model name>_detail.html by default, unless overwritten by template_name
    # generic view expects the primary key value captured from the URL to be called 'pk', which is implemented in urls.py


# ############### image upload
# @login_required
def post(request):
    ImageFormSet = modelformset_factory(PropertyImages, form=ImageForm, extra=30)

    if request.method == 'POST':
        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=PropertyImages.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                if form:
                    image=form['image']
                    photo=PropertyImages(post=post_form, image=image)
                    photo.save()
            messages.success(request,"Upload success!")
            return HttpResponseRedirect("/")

        else:
            print(postForm.errors, formset.errors)
        
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=PropertyImages.objects.none())
    return render(request, 'global_listing/post.html', {'postForm': postForm, 'formset': formset})