from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from musicapp.albums.models import Album
from musicapp.profiles.form import ProfileCreateForm
from musicapp.utils import get_user_obj

class HomePage(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')
    

    def get_template_names(self):
        profile = get_user_obj()

        if profile:
            return ['profile/home-with-profile.html']
        else:
            return ['profile/home-no-profile.html']
        
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
