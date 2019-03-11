############ Form and Image Upload

from django import forms
from .models import *

class PostForm(forms.ModelForm):
    post_title = forms.CharField(max_length=128)
    description = forms.CharField(max_length=2450, label="Description")
    
    class Meta:
        model = Property
        fields = ('post_title', 'description',)

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = PropertyImages
        fields = ('image',)