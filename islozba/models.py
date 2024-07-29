from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    style = [
        ("IMP", "impressionism"),
        ("POP", "pop art"),
        ("GRA", "graffiti")
    ]
    type = models.CharField(choices=style, blank=True, null=True, max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.surname}'


class Exhibition(models.Model):
    title = models.CharField(max_length=30)
    date_start = models.DateField()
    date_end = models.DateField()
    description = models.TextField(max_length=255)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Artwork(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField()
    image = models.ImageField(upload_to='islozba/')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
