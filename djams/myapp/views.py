from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime

from .models import *

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import *
# Create your views here.


class SongViewSet(viewsets.ModelViewSet):

    queryset = Song.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return SongWriteSerializer
        return SongReadOnlySerializer


class GenreViewSet(viewsets.ModelViewSet):

    queryset = Genre.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return GenreWriteSerializer
        return GenreReadOnlySerializer


class ArtistViewSet(viewsets.ModelViewSet):

    queryset = Artist.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return ArtistWriteSerializer
        return ArtistReadOnlySerializer


class AlbumViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return AlbumWriteSerializer
        return AlbumReadOnlySerializer


# class PlaylistViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows groups to be viewed or edited.
#    """
#    queryset = Group.objects.all()
#    serializer_class = PlaylistSerializer
#
