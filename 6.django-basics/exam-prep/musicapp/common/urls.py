from django.urls import path
from musicapp.common.views import HomePage


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]