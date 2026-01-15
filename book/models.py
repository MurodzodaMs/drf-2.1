from django.db import models
from accounts.models import CustomUser as User

class Book(models.Model):
    GENRE_CHOICES = [
        ('fantasy', 'fantasy'),
        ('fantastic', 'fantastic'),
        ('detective', 'detective'),
        ('novel', 'novel'),
        ('fiction', 'fiction'),
        ('science', 'science'),
        ('history', 'history'),
        ('fairy_tale', 'fairy_tale'),
        ('other', 'Другие'),
    ]

    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='books'
    )
    publication_year = models.PositiveIntegerField()
    genre = models.CharField(
        max_length=50,
        choices=GENRE_CHOICES
    )

    def __str__(self):
        return self.title
