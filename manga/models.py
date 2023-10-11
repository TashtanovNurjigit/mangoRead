from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Manga(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image_manga')
    synopsis = models.TextField()
    release = models.IntegerField()
    type_manga = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre, blank=True)

    @property
    def reviews_manga(self):
        return self.reviews_manga.all()

    def __str__(self):
        return self.name


class Reviews(models.Model):
    text = models.TextField()
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='reviews_manga')

    def __str__(self):
        return self.text
