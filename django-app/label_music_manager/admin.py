from django.contrib import admin
from .models import Album, Song, AlbumTracklistItem, MusicManagerUser

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Song)
admin.site.register(AlbumTracklistItem)
admin.site.register(MusicManagerUser)


