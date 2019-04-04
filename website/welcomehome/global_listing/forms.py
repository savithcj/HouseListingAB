############ Form and Image Upload

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *
from phonenumber_field.formfields import PhoneNumberField

class SignUpForm(UserCreationForm):
    phone_day = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}),label="Phone number", required=False)

    class Meta:
        model = User
        fields = ('username','email','phone_day','password1','password2', )


class RoomSpaceForm(forms.ModelForm):

    class Meta:
        model = RoomSpace
        exclude = ('property_id','room_id')

RoomSpaceFormSet = inlineformset_factory(
    Property, RoomSpace, form=RoomSpaceForm,
    fields=['name','description','ceiling_heights','is_insulated','num_of_windows','fireplace','size'], 
    extra=1,can_delete=True, can_order=True,
    max_num=30,
)

class PostForm(forms.ModelForm):
    post_title = forms.CharField(max_length=128, required=True, widget=forms.TextInput(attrs={'placeholder':'a catchy descriptive title'}))
    description = forms.CharField(max_length=2450, required=True, widget=forms.Textarea(attrs={'placeholder':"My beautiful home up for sale has...",'rows': 6, 'cols': 50}))
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
        exclude = ()

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user_instance')
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('post_title'),
                Field('price'),
                Field('residence_type'),
                Field('above_grade_sqft'),
                Field('description'),
                Field('lot_size'),
                Field('is_residential'),
                Field('is_commercial'),
                Field('num_of_buildings'),
                Fieldset('Add room',
                    Formset('room_form')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
                )
            )

    def clean_user(self):
        return self.user.user_profile


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = PropertyImages
        fields = ('image',)