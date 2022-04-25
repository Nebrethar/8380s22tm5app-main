from django.contrib import admin
from .models import PlaylistModel

@admin.register(PlaylistModel)
class PlaylistModelAdmin(admin.ModelAdmin):

    list_display = ["playlist_id", "playlist_name", "song", "artist", "album", "source"]