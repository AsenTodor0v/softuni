from django.shortcuts import  get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import  DetailView, UpdateView
from furryfunnies.posts.forms import DeletePostForm, EditPostForm, PostForm
from furryfunnies.posts.models import Post
from furryfunnies.utils import get_profile

# Create your views here.

def create_post_page(request):
    form = PostForm(request.POST or None)
    profile = get_profile()
    if form.is_valid():
        form.instance.author_id = profile.pk
        form.save()

        return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, template_name='posts/create-post.html', context=context)


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'posts/details-post.html'


class PostEditView(UpdateView):
    model = Post
    form_class = EditPostForm
    pk_url_kwarg = 'post_id'
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dashboard')


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('dashboard')

    form = DeletePostForm(instance=post)
    context = {
        'profile': get_profile(),
        'form': form
    }

    return render(request, 'posts/delete-post.html', context)