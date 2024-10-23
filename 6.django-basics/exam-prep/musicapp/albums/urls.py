from django.urls import include, path

from musicapp.albums.views import AlbumCreateView, AlbumDeleteView, AlbumDetailView, AlbumEditView


urlpatterns = [
    path('add/', AlbumCreateView.as_view(), name='add-album'),
    path('<int:id>/', include([
        path('edit/', AlbumEditView.as_view(), name='edit-album'),
        path('details/', AlbumDetailView.as_view(), name='details-album'),
        path('delete/', AlbumDeleteView.as_view(), name='delete-album'),
    ]))
]