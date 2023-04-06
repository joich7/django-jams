from django.db import models

# Create your models here.


class Song(models.Model):
    name = models.CharField(max_length=100, null=True)
    # album = models.ForeignKey('Genre', on_delete=models.PROTECT, null=True)
    album = models.ForeignKey('Album', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=100, null=True)
    song = models.ManyToManyField(Song)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=100, null=True)
    artist = models.ManyToManyField(Artist)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name
