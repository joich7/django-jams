from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class SongReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['name', 'album']


class SongWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['name', 'album']


# class PlaylistSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Playlist
#        fields = ['name', 'song']
#

# Gere Serialisers
class GenreReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name',]


class GenreWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name',]

# Artist Serializers


class ArtistReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name',]


class ArtistWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name',]

# ALbum Serializers


class AlbumReadOnlySerializer(serializers.ModelSerializer):
    class Meta:

        model = Album
        fields = ['name', 'songs']


class AlbumWriteSerializer(serializers.ModelSerializer):
    class Meta:
        songs = SongReadOnlySerializer(many=True, source='song')
        model = Album
        fields = ['name', 'songs']
