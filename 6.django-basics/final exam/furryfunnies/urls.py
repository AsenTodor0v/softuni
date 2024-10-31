from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('furryfunnies.common.urls')),
    path('authors/', include('furryfunnies.authors.urls')),
    path('posts/', include('furryfunnies.posts.urls')),
]
