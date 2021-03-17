import logging

from django.conf import settings

from yt_arch import models
from .api_client import ApiClient

log = logging.getLogger(__name__)


class Fetcher:
    max_page_size = 50

    def __init__(self):
        self.api = ApiClient()
        self.api_key = settings.YT_API_KEY

    def fetch(self, playlist_id):
        log.info('Fetching playlist %s', playlist_id)

        playlist, _ = models.Playlist.objects.get_or_create(external_id=playlist_id)
        playlist_version = models.PlaylistVersion.objects.create(playlist=playlist)

        next_page_token = ''
        while next_page_token is not None:
            ret = self.api.get('playlistItems', params={
                'key': self.api_key,
                'part': 'snippet',
                'playlistId': playlist_id,
                'maxResults': self.max_page_size,
                'pageToken': next_page_token,
            })
            next_page_token = ret.get('nextPageToken')

            for item in ret['items']:
                self._append(playlist_version, item['snippet'])

    def _append(self, playlist_version, snippet):
        external_id = snippet['resourceId']['videoId']
        meta, _ = models.VideoMeta.objects.get_or_create(external_id=external_id, defaults={
            'title': snippet['title'],
            'channel_id': snippet.get('videoOwnerChannelId', ''),
            'published_at': snippet['publishedAt'],
        })

        item = models.PlaylistItem()
        item.playlist_version = playlist_version
        item.position = snippet['position']
        item.video_meta = meta
        item.save()

        log.info('%d. %s', item.position, meta.title)
