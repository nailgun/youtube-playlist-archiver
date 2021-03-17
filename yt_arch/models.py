from django.db import models
from utils.django.apps.users.models import AbstractUser


class Playlist(models.Model):
    external_id = models.CharField(max_length=255)

    def __str__(self):
        return self.external_id


class PlaylistVersion(models.Model):
    playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE)
    fetched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.fetched_at)


class PlaylistItem(models.Model):
    playlist_version = models.ForeignKey('PlaylistVersion', on_delete=models.CASCADE)
    position = models.IntegerField()
    video_meta = models.ForeignKey('VideoMeta', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.position}. {self.video_meta}'


class VideoMeta(models.Model):
    external_id = models.CharField(max_length=32, unique=True)
    title = models.CharField(max_length=255, blank=True)
    channel_id = models.CharField(max_length=64, blank=True)
    published_at = models.DateTimeField(blank=True, null=True)
    discovered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.external_id} — {self.title}'


class User(AbstractUser):
    pass
