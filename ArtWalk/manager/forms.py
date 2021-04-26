from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('is_artisan',)


class BoothForm(forms.ModelForm):
    class Meta:
        model = Booth
        fields = ('name', 'description', 'cover_image', 'twitch_name', )


class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ('name', 'description', 'image', 'price')