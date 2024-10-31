from django.db import models
from django.core.validators import MinLengthValidator
from furryfunnies.authors.validators import only_letters, exact_length
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=(
            MinLengthValidator(2),
            only_letters,
        )
        )
    
    last_name = models.CharField(
        max_length=50,
        validators=(
            MinLengthValidator(2),
            only_letters,
        )
        )
    
    passcode = models.CharField(
        validators=(
            exact_length,
        ),
        help_text="Your passcode must be a combination of 6 digits",
    )

    pets_number = models.PositiveSmallIntegerField(

    )

    info = models.TextField(
        null=True,
        blank=True
    )

    image_url = models.URLField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    