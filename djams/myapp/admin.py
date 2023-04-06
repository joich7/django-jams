from django.contrib import admin

# Register your models here.
from .models import Song, Artist, Album, Playlist, Genre
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Playlist)
admin.site.register(Genre)
