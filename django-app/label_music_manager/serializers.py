# Write your serialisers here
#it Convert Django models to JSON data and vice versa.

#serializers are used to convert complex data types, such as Django model instances, 
# into native Python data types (such as dictionaries, lists, etc.) that can then be rendered into 
# JSON, XML, or other content types. This is particularly useful when working with Django REST Framework (DRF) to create APIs.


# label_music_manager/serializers.py

from rest_framework import serializers
from .models import Album, Song, AlbumTracklistItem
#from rest_framework.models.permissions import DjangoPermissions

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'running_time']


class AlbumSerializer(serializers.ModelSerializer):

    short_description = serializers.SerializerMethodField()
    release_year = serializers.SerializerMethodField()
    total_playtime = serializers.SerializerMethodField()
    tracklist = serializers.SerializerMethodField()
    songs = serializers.SerializerMethodField()  # Read-only field for tracklist details

    class Meta:
        model = Album
        fields = [
            'id', 'title', 'artist', 'price', 'release_date', 'cover_image',
            'short_description', 'release_year', 'total_playtime', 'tracklist','songs',
        ]
        

    def get_short_description(self, obj):
        if obj.description:
            return obj.description[:255] + ('…' if len(obj.description) > 255 else '')
        return None

    def get_release_year(self, obj):
        return obj.release_date.year if obj.release_date else None

    def get_total_playtime(self, obj):
        # Sum the running time of all songs in the album's tracklist
        return sum(item.song.running_time for item in obj.tracklist_items.all())

    def get_tracklist(self, obj):
        # Generate hypermedia links for each track in the album
        request = self.context.get('request')  # Use request context for building absolute URLstracklist_items = obj.tracklist_items.order_by('position')    

        return [
            {
                'id': item.song.id,
                'title': item.song.title,
                'position': item.position,
                'link': request.build_absolute_uri(f'/api/songs/{item.song.id}/')
            }
            for item in obj.tracklist_items.all()
        ]
    
    def get_songs(self, obj):
        # Serialize songs from the tracklist
        return [
            {
                'id': item.song.id,
                'title': item.song.title,
                'position': item.position,
            }
            for item in obj.tracklist_items.order_by('position')
        ]
    
    def create(self, validated_data):
        songs_data = validated_data.pop('songs', [])
        album = Album.objects.create(**validated_data)

        # Add songs to the tracklist
        for i, song_id in enumerate(songs_data):
            song = Song.objects.get(id=song_id)
            AlbumTracklistItem.objects.create(album=album, song=song, position=i+1)

        return album
    
    def get_edit_link(self, obj):
        request = self.context.get('request')
        if request and request.user.has_perm('label_music_manager.change_album'):
            return request.build_absolute_uri(f'/api/albums/{obj.id}/edit/')
        return None

    def get_delete_link(self, obj):
        request = self.context.get('request')
        if request and request.user.has_perm('label_music_manager.delete_album'):
            return request.build_absolute_uri(f'/api/albums/{obj.id}/delete/')
        return None


class AlbumTracklistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumTracklistItem
        fields = ['id', 'album', 'song', 'position']
        extra_kwargs = {
            'album': {'read_only': True}, 
        }



    class Meta:
        model = AlbumTracklistItem
        fields = ['album', 'song', 'position']

    def get_total_playtime(self, obj):
        # Calculate total playtime as the sum of all song running times in the album
        return sum(item.song.running_time for item in obj.tracklist_items.all())    


