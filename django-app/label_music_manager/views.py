# Use this file for your templated views only
# label_music_manager/views.py

from django.shortcuts import render
from django.http import Http404
from .models import Album, Song, AlbumTracklistItem

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'label_music_manager/album_list.html', {'albums': albums})

def album_detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    
    songs = Song.objects.filter(albumtracklistitem__album=album)
    return render(request, 'label_music_manager/album_detail.html', {'album': album, 'songs': songs})

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'label_music_manager/song_list.html', {'songs': songs})

def song_detail(request, song_id):
    try:
        song = Song.objects.get(pk=song_id)
    except Song.DoesNotExist:
        raise Http404("Song does not exist")
    
    return render(request, 'label_music_manager/song_detail.html', {'song': song})

def album_tracklist(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    
    tracklist_items = AlbumTracklistItem.objects.filter(album=album)
    return render(request, 'label_music_manager/album_tracklist.html', {'album': album, 'tracklist_items': tracklist_items})
