############ Form and Image Upload

from django import forms
from .models import *

class RoomSpaceMixin(forms.ModelForm):
    
    class Meta:
        model = RoomSpace
        fields = ('name', 'description', 'ceiling_heights', 'is_insulated', 'num_of_windows','fireplace', 'size')

class PostForm(forms.ModelForm):

    post_title = forms.CharField(max_length=128, required=True, help_text="Catchy decriptive title for your posting", initial="")
    description = forms.CharField(max_length=2450, required=True, help_text="Describe your home in a paragraph", initial="My beautiful home up for sale has...")
    price = forms.FloatField(required=True)
    above_grade_sqft = forms.FloatField(required=True)
    lot_size = forms.FloatField(required=False)
    is_commercial = forms.BooleanField(required=False)

    OPTIONS = (
            ("House", "House"),
            ("Duplex", "Duplex"),
            ("Townhouse", "Townhouse"),
            ("Highrise", "Highrise"),
            ("Lowrise", "Lowrise"),
            ("Mobile", "Mobile")
            )
    residence_type = forms.TypedMultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)

    class Meta:
        model = Property
        fields = ('post_title', 'description', 'price', 'above_grade_sqft', 'lot_size', 'is_commercial', 'residence_type')
        widgets = {
            'post_title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
        }

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = PropertyImages
        fields = ('image',)