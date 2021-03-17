from django.db import models


class Playlist(models.Model):
    external_id = models.CharField(max_length=255)


class PlaylistVersion(models.Model):
    playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE)
    fetched_at = models.DateTimeField(auto_now_add=True)


class PlaylistItem(models.Model):
    playlist_version = models.ForeignKey('PlaylistVersion', on_delete=models.CASCADE)
    position = models.IntegerField()
    video_meta = models.ForeignKey('VideoMeta', on_delete=models.PROTECT)


class VideoMeta(models.Model):
    external_id = models.CharField(max_length=32, unique=True)
    title = models.CharField(max_length=255)
    channel_id = models.CharField(max_length=64)
    published_at = models.DateTimeField()
    discovered_at = models.DateTimeField(auto_now_add=True)
