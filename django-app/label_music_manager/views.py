# Use this file for your templated views only
# label_music_manager/views.py

from django.shortcuts import render, redirect,get_object_or_404
from django.http import Http404
from django.urls import reverse
from .models import Album, Song, AlbumTracklistItem,MusicManagerUser
from .forms import AlbumForm
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to MyMusicMaestro!")

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'label_music_manager/album_list.html', {'albums': albums})

def album_detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    
    # Fetch the related tracklist entries for this album
    tracklist_items = AlbumTracklistItem.objects.filter(album=album)
    
    # Fetch the songs associated with this album's tracklist items
    songs = [tracklist_item.song for tracklist_item in tracklist_items]
    
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


@login_required
@permission_required('label_music_manager.add_album', raise_exception=True)
def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_list')  # Redirect to the album list view after saving
    else:
        form = AlbumForm()
    return render(request, 'label_music_manager/create_album.html', {'form': form})

@login_required
@permission_required('label_music_manager.change_album', raise_exception=True)
def edit_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_detail', album_id=album.id)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'label_music_manager/edit_album.html', {'form': form, 'album': album})

