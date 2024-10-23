from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('musicapp.common.urls')),
    path('album/', include('musicapp.albums.urls')),
    path('profile/', include('musicapp.profiles.urls')),
]
