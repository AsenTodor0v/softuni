from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from musicapp.albums.forms import AlbumCreateForm, AlbumDeleteForm
from musicapp.albums.models import Album
from musicapp.utils import get_user_obj

# Create your views here.
class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'album/album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)
    
class AlbumEditView(UpdateView):
    model = Album
    form_class = AlbumCreateForm
    pk_url_kwarg = 'id'
    template_name = 'album/album-edit.html'
    success_url = reverse_lazy('home')


class AlbumDetailView(DetailView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'album/album-details.html'

class AlbumDeleteView(DeleteView):
    model = Album
    form_class = AlbumDeleteForm
    pk_url_kwarg = 'id'
    template_name = 'album/album-delete.html'
    success_url = reverse_lazy('home')
    
    def get_initial(self):
        return self.object.__dict__
    
    def form_invalid(self, form):
        return self.form_valid(form)
    