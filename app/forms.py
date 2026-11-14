from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ValidationError

class Registerform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']

class Profileform(forms.ModelForm):
    # phone = forms.IntegerField(validators=['tendigit'])
    class Meta:
        model = Profile
        # fields = "__all__"
        exclude = ['user']

        widgets = {
        'bio': forms.TextInput(attrs={
        'class' :'form-control',
        'placeholde':'enter your  bio'
        }),
     }
    def clean(self):
        cleaned_data = super().clean()
        phone =cleaned_data.get('phone')
        if len(str(phone)) != 10:
            raise forms.ValidationError(
                "phone must be equalto 10 digits."
            )
        return cleaned_data