from django.urls import path

from furryfunnies.authors import views

urlpatterns = [
    path('create/', views.create_author_page, name='create-author'),
    path('details/', views.AuthorDetailView.as_view(), name='author-details'),
    path('edit/', views.AuthorEditView.as_view(), name='author-edit'),
    path('delete/', views.delete_author_page, name='delete-author'),
]
