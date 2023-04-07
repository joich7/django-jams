from django.db import models

# Create your models here.


# class Playlist(models.Model):
#    name = models.CharField(max_length=500, null=True)
#    song = models.ManyToManyField('Song')
#
#    def __str__(self):
#        return self.name
#

class Song(models.Model):

    name = models.CharField(max_length=500, null=True)
    # album = models.ForeignKey('Genre', on_delete=models.PROTECT, null=True)
    album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True)
    artist = models.ManyToManyField('Artist')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    artist = models.ManyToManyField('Artist')
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        return self.name
