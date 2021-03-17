from django.contrib import admin
from yt_arch import models


@admin.register(models.Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('external_id',)


class PlaylistItemInline(admin.TabularInline):
    model = models.PlaylistItem
    autocomplete_fields = ('video_meta',)
    extra = 0


@admin.register(models.PlaylistVersion)
class PlaylistVersionAdmin(admin.ModelAdmin):
    list_display = ('fetched_at', 'playlist',)
    ordering = ('-fetched_at',)
    list_filter = ('playlist',)
    inlines = [PlaylistItemInline]


@admin.register(models.VideoMeta)
class VideoMetaAdmin(admin.ModelAdmin):
    list_display = ('external_id', 'title', 'channel_id', 'published_at', 'discovered_at',)
    ordering = ('-discovered_at',)
    readonly_fields = ('discovered_at',)
    search_fields = ('external_id',)
