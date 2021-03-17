from django.core.management.base import BaseCommand, CommandError

from yt_arch import models, core


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('playlist_ids', nargs='*')

    def handle(self, playlist_ids, **options):
        if not playlist_ids:
            self.stdout.write('Playlist IDs not specified, fetching saved playlists')
            playlist_ids = list(models.Playlist.objects.values_list('external_id', flat=True))

        fetcher = core.Fetcher()
        for pl_id in playlist_ids:
            fetcher.fetch(pl_id)
