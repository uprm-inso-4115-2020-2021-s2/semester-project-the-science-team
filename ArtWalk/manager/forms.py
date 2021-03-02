from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('is_artist',)