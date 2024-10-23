from django.urls import path

from musicapp.profiles.views import ProfileDeleteView, ProfileDetailView


urlpatterns = [
    path('details/', ProfileDetailView.as_view(), name='profile-details'),
    path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
]