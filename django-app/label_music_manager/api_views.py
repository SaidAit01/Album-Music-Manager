# Use this file for your API viewsets only
# E.g., from rest_framework import ...

from django.forms import ValidationError
from rest_framework import viewsets
from .models import Album, Song, AlbumTracklistItem
from .serializers import AlbumSerializer, SongSerializer, AlbumTracklistItemSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions,AllowAny


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows albums to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [AllowAny]  # Ensure only authenticated users can access albums
    def get_serializer_context(self):
        # Pass the request context to the serializer for generating URLs
        return {'request': self.request}


class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows songs to be viewed or edited.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]


class AlbumTracklistItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows album tracklist items to be viewed or edited.
    """
    queryset = AlbumTracklistItem.objects.all()
    serializer_class = AlbumTracklistItemSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def perform_create(self, serializer):
        # Retrieve the album ID from the request data
        album_id = self.request.data.get('album')
        if not album_id:
            raise ValidationError({"album": "This field is required."})

        # Retrieve the album instance
        try:
            album = Album.objects.get(id=album_id)
        except Album.DoesNotExist:
            raise ValidationError({"album": "The album with the provided ID does not exist."})

        # Save the serializer with the associated album
        serializer.save(album=album)

