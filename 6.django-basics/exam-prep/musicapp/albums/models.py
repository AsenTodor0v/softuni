from django.db import models
from django.core.validators import MinValueValidator
from musicapp.albums.choices import GenreChoices

class Album(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False
        )
    
    artist = models.CharField(
        max_length=30,
        null=False,
        blank=False
        )
    
    genre = models.CharField(
        max_length=30,
        choices=GenreChoices.choices,
        )
    
    description = models.TextField(
        null=True,
        blank=True
        )
    
    image_url = models.URLField(
        null=False,
        blank=False
        )
    
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(0.0),
        )
    )

    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name="albums",
    )