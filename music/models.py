from django.db import models

# Create your models here.
class PlaylistModel(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    playlist_name = models.CharField(blank=True, max_length=100)
    song = models.CharField(blank=True, max_length=100)
    artist = models.CharField(blank=True, max_length=100)
    album = models.CharField(blank=True, max_length=100)
    yt_link = models.CharField(blank=True, max_length=100)
    sf_link = models.CharField(blank=True, max_length=100)
    source = models.CharField(blank=True, max_length=100)
    username = models.CharField(blank=True, max_length=100)

    def __str__(self):
            return self.playlist_name

    class Meta:
        verbose_name = "Playlist"
        verbose_name_plural = "Playlists"