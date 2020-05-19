from django.contrib import admin
from .models import Song, Artist, Genre, Album

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_id', 'title']

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    
