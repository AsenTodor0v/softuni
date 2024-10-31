from django.urls import include, path

from furryfunnies.posts import views

urlpatterns = [
    path('create/', views.create_post_page, name='create-post'),
    path('<post_id>/', include([
        path('details/', views.PostDetailView.as_view(), name='post-details'),
        path('edit/', views.PostEditView.as_view(), name='post-edit'),
        path('delete/', views.delete_post, name='post-delete'),
    ]))
]
