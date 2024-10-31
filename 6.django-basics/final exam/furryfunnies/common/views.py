from django.shortcuts import render

from furryfunnies.authors.models import Author
from furryfunnies.posts.models import Post
from furryfunnies.utils import get_profile
# Create your views here.
def index(request):
    author = Author.objects.first()
    context = {'author': author}

    return render(request, template_name='index.html', context=context)

def dashboard(request):
    posts = Post.objects.all()
    context = {'posts': posts,
               'profile': get_profile()}

    return render(request, template_name='dashboard.html', context=context)