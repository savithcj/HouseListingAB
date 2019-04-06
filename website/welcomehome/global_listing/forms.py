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

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_day', 'phone_alt']

class ImageForm(forms.ModelForm):
    image = forms.ImageField(required=True)

    class Meta:
        model = PropertyImages
        exclude= ()

class RoomSpaceForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder':'ie: Kitchen, Living Room, Bedroom, etc.'}))

    shape_options = (
        (0, "Square/Rectangle"),
        (1, "Round"),
        (2, "Irregular"),
        (3, "Other"),
    )

    flooring_options = (
        (0, "Carpet"),
        (1, "Laminated"),
        (2, "Hard Wood"),
        (3, "Wood/Polymer Composite"),
        (4, "Vinyl"),
        (5, "Painted/Epoxy"),
        (6, "Unfinished Concrete"),
        (7, "Other"),
    )

    flooring = forms.ChoiceField(choices=flooring_options, required=False, initial=None)
    shape = forms.ChoiceField(choices=shape_options, required=False, initial=None)

    class Meta:
        model = RoomSpace
        exclude = ()

RoomSpaceFormSet = inlineformset_factory(
    Property, RoomSpace, form=RoomSpaceForm,
    fields=['name','description','floor_level','shape','dimA','dimB','flooring','fireplace','ceiling_heights','num_of_windows','sqft','is_insulated',], 
    extra=1, can_delete=True, can_order=True,
    max_num=30,
)

ImageFormSet = inlineformset_factory(Property, PropertyImages, form=ImageForm, 
    fields =['image','title'],
    extra=1, can_delete=True, can_order=True,
    max_num=30,
)

class PostForm(forms.ModelForm):
    post_title = forms.CharField(max_length=128, required=True, widget=forms.TextInput(attrs={'placeholder':'a catchy descriptive title'}))
    description = forms.CharField(max_length=2450, required=True, widget=forms.Textarea(attrs={'placeholder':"My beautiful home up for sale has...",'rows': 6, 'cols': 50}))
    
    is_active = forms.TypedChoiceField(
        coerce = lambda x: x == 'True',
        choices = ((True, 'Activate Listing'), (False, 'Deactivate Listing')),
        initial = True,
        widget = forms.RadioSelect,
    )

    price = forms.FloatField(required=True)
    above_grade_sqft = forms.FloatField(required=True)
    lot_size = forms.FloatField(required=False)
    is_residential = forms.BooleanField(required=False)
    residence_options = (
            ("House", "House"),
            ("Duplex", "Duplex"),
            ("Townhouse", "Townhouse"),
            ("Highrise", "Highrise"),
            ("Lowrise", "Lowrise"),
            ("Mobile", "Mobile"),
            ("Hut", "Hut"),
            )
    residence_type = forms.ChoiceField(choices=residence_options, required=False)
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
                Field('is_active'),
                Field('post_title'),
                Field('price'),
                Field('residence_type'),
                Field('above_grade_sqft'),
                Field('description'),
                Field('lot_size'),
                Field('is_residential'),
                Field('is_commercial'),
                Field('num_of_buildings'),
                Fieldset('Add room',Formset('room_form')),
                Fieldset('Add image',ImageFormset('image_form')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
                )
            )

    def clean_user(self):
        """The clean_<fieldname>() method is called on a form subclass – where <fieldname> is replaced
         with the name of the form field attribute. This method does any cleaning that is specific
         to that particular attribute, unrelated to the type of field that it is. This method is not 
        passed any parameters. You will need to look up the value of the field in self.cleaned_data 
        and remember that it will be a Python object at this point, not the original string submitted 
        in the form (it will be in cleaned_data because the general field clean() method, above, 
        has already cleaned the data once)."""
        return self.user.user_profile


