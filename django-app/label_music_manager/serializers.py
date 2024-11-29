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
        fields = ['id', 'name', 'release_date', 'cover_image', 'songs']

class AlbumTracklistItemSerializer(serializers.ModelSerializer):
    song = SongSerializer()

    class Meta:
        model = AlbumTracklistItem
        fields = ['song', 'position']
