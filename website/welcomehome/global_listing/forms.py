############ Form and Image Upload

from django import forms
from .models import *

class RoomSpaceMixin(forms.ModelForm):
    
    class Meta:
        model = RoomSpace
        fields = ('name', 'description', 'ceiling_heights', 'is_insulated', 'num_of_windows','fireplace', 'size')

class PostForm(forms.ModelForm):

    post_title = forms.CharField(max_length=128, required=True, widget=forms.TextInput(attrs={'placeholder':'a catchy descriptive title'}))
    description = forms.CharField(max_length=2450, required=True, widget=forms.Textarea(attrs={'placeholder':"My beautiful home up for sale has...",'rows': 4, 'cols': 25}))
    price = forms.FloatField(required=True)
    above_grade_sqft = forms.FloatField(required=True)
    lot_size = forms.FloatField(required=False)
    is_residential = forms.BooleanField(required=False)
    OPTIONS = (
            ("House", "House"),
            ("Duplex", "Duplex"),
            ("Townhouse", "Townhouse"),
            ("Highrise", "Highrise"),
            ("Lowrise", "Lowrise"),
            ("Mobile", "Mobile")
            )
    residence_type = forms.TypedMultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS)
    is_commercial = forms.BooleanField(required=False)
    num_of_buildings = forms.IntegerField(required=False)

    class Meta:
        model = Property
        fields = ('post_title','description','price','above_grade_sqft','lot_size','is_residential','residence_type','is_commercial','num_of_buildings')
        

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = PropertyImages
        fields = ('image',)