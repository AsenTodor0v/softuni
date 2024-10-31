from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from furryfunnies.authors.forms import AuthorForm, DeleteAuthorForm, EditAuthorForm
from furryfunnies.authors.models import Author
from furryfunnies.utils import get_profile

# Create your views here.
def create_author_page(request, ):
    form = AuthorForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}

    return render(request, template_name='authors/create-author.html', context=context)

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/details-author.html'
    context_object_name = 'author'
    def get_object(self, queryset = None):
        return get_profile()
    

class AuthorEditView(UpdateView):
    model = Author
    template_name = 'authors/edit-author.html'
    success_url = reverse_lazy('author-details')
    form_class = EditAuthorForm
    def get_object(self, queryset = None):
        return get_profile()
    
def delete_author_page(request):
    author = get_profile()
    form = DeleteAuthorForm(instance=author)

    if request.method == 'POST':
        author.delete()
        return redirect('index')

    context = {
        'author': author,
        'form': form,
    }

    return render(request, 'authors/delete-author.html', context)