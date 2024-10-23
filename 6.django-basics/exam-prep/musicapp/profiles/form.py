from musicapp.profiles.models import Profile
from django import forms

class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'

class ProfileCreateForm(ProfileCreateForm):
    pass