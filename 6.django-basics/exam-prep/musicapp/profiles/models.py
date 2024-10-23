from django.db import models
from django.core.validators import MinLengthValidator

from musicapp.profiles.validators import validate_username

class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            validate_username
        ),
        null=False,
        blank=False,
        )
    
    email = models.EmailField(
        null=False,
        blank=False
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )