# Write your serialisers here
#it Convert Django models to JSON data and vice versa.

#serializers are used to convert complex data types, such as Django model instances, 
# into native Python data types (such as dictionaries, lists, etc.) that can then be rendered into 
# JSON, XML, or other content types. This is particularly useful when working with Django REST Framework (DRF) to create APIs.


# label_music_manager/serializers.py

from rest_framework import serializers
from .models import Album, Song, AlbumTracklistItem

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'running_time', 'position', 'albums']

class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)  # Read-only nested serializer

    class Meta:
        model = Album
        fields = ['id', 'title', 'release_date', 'cover_image', 'songs',]

from rest_framework import serializers
from label_music_manager.models import Album, Song

class AlbumSerializer(serializers.ModelSerializer):
    short_description = serializers.SerializerMethodField()
    release_year = serializers.SerializerMethodField()
    total_playtime = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'release_date', 'short_description', 'release_year', 'total_playtime', 'tracklist_items']

    def get_short_description(self, obj):
        return f"{obj.description[:255]}..." if obj.description else ""

    def get_release_year(self, obj):
        return obj.release_date.year

    def get_total_playtime(self, obj):
        total_playtime = Song.objects.filter(album=obj).aggregate(total=Sum('running_time'))['total']
        return total_playtime if total_playtime else 0

