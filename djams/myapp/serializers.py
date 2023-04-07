from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class SongReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'album']


class SongWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'album']


# class PlaylistSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Playlist
#        fields = ['name', 'song']
#

# Gere Serialisers
class GenreReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name',]


class GenreWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name',]

# Artist Serializers


class ArtistReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name',]


class ArtistWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name',]

# ALbum Serializers


class AlbumReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        songs = SongReadOnlySerializer(many=True, source='song')
        model = Album
        fields = ['id', 'name', 'songs','artist','genre']


class AlbumWriteSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Album
        fields = ['id', 'name', 'songs']
