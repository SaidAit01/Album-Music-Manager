# Use this file for your API viewsets only
# E.g., from rest_framework import ...

from rest_framework import viewsets
from .models import Album, Song, AlbumTracklistItem
from .serializers import AlbumSerializer, SongSerializer, AlbumTracklistItemSerializer
from rest_framework.permissions import IsAuthenticated


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows albums to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access albums
    
def get_queryset(self):
        # If an artist is logged in, filter albums by the artist's name
        user = self.request.user
        if user.is_authenticated:
            return Album.objects.filter(artist=user.display_name)
        return Album.objects.all()


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
    permission_classes = [IsAuthenticated]

