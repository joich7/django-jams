from django.db import models

# Create your models here.


class Song(models.Model):
    name = models.CharField(max_length=100)
    #album = models.ForeignKey('Genre', on_delete=models.PROTECT, null=True)


class Album(models.Model):
    name = models.CharField(max_length=100)


class Playlist(models.Model):
    name = models.CharField(max_length=100)


class Genre(models.Model):
    name = models.CharField(max_length=100)
