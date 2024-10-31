from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Post(models.Model):
    title = models.CharField(
        unique=True,
        max_length=50,
        validators=(
            MinLengthValidator(2),
        ),
        error_messages={
            "unique": "Oops! That title is already taken. How about something fresh and fun?",
        }
    )

    image_url = models.URLField(
        help_text='Share your funniest furry photo URL!'
    )

    content = models.TextField()

    updated_at = models.DateTimeField(
        auto_now=True,
        )
    
    author = models.ForeignKey(
        'authors.Author',
        on_delete=models.CASCADE,
        related_name='posts'

    )
