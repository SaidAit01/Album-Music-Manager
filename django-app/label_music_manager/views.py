# label_music_manager/views.py
import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseForbidden
from .models import Album, Song, AlbumTracklistItem
from .forms import AlbumForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.views.decorators.http import require_GET

logger = logging.getLogger(__name__)

@login_required
@permission_required('label_music_manager.album_list', raise_exception=True)
def album_list(request):
    user = request.user
    logger.info(f"User: {user.username}, is_superuser: {user.is_superuser}")

    if user.is_superuser:
        logger.info("Superuser detected. Showing all albums.")
        albums = Album.objects.all()
    elif hasattr(user, 'musicmanageruser'):
        logger.info(f"User role: {getattr(user.musicmanageruser, 'role', 'No Role Found')}")
        role = user.musicmanageruser.role

        if role == 'artist':
            logger.info("Artist detected. Filtering albums by artist name.")
            albums = Album.objects.filter(artist=user.musicmanageruser.display_name)
        elif role == 'viewer':
            logger.info("Viewer detected. Showing all albums.")
            albums = Album.objects.all()
        elif role == 'editor':
            logger.info("Editor detected. Showing all albums with edit permissions.")
            albums = Album.objects.all()
        else:
            logger.warning("User role not recognized. Returning insufficient permissions.")
            return HttpResponseForbidden("User role not defined or insufficient permissions.")
    else:
        logger.warning("User role not defined or insufficient permissions.")
        return HttpResponseForbidden("User role not defined or insufficient permissions.")

    return render(request, 'label_music_manager/album_list.html', {'albums': albums})


@login_required
@permission_required('label_music_manager.album_detail', raise_exception=True)

def album_detail(request, album_id, slug=None):
 
    album = get_object_or_404(Album, pk=album_id)

    # If a slug is provided and it doesn't match, redirect to the correct slug URL
    if slug and slug != album.slug:
        return redirect('album_detail_with_slug', album_id=album.id, slug=album.slug)
    

    # Retrieve the album's tracklist and associated songs
    tracklist_items = AlbumTracklistItem.objects.filter(album=album)
    songs = [item.song for item in tracklist_items]

    # Render the album detail template
    return render(request, 'label_music_manager/album_detail.html', {
        'album': album,
        'songs': songs,
    })

@login_required
@permission_required('label_music_manager.create_album', raise_exception=True)
def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            
            album = form.save()

            # Handle adding tracks via the AlbumTracklistItem model (separate from album creation)
            songs = request.POST.getlist('songs')  # Get selected song IDs
            for i, song_id in enumerate(songs):
                song = Song.objects.get(id=song_id)
                position = i + 1  # Position is set based on the order in the form submission
                AlbumTracklistItem.objects.create(album=album, song=song, position=position)

            # Redirect to the album list after successful creation
            return redirect('album_list')
    else:
        form = AlbumForm()

    return render(request, 'label_music_manager/create_album.html', {'form': form})

@login_required
@permission_required('label_music_manager.edit_album', raise_exception=True)
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

@login_required
@permission_required('label_music_manager.delete_album', raise_exception=True)
def delete_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    # Check if the user is an artist of the album or an editor
    if album.artist != request.user and not request.user.has_perm('label_music_manager.delete_album'):
        return HttpResponseForbidden("You do not have permission to delete this album.")

    if request.method == 'POST':
        album.delete()
        return redirect('album_list')  # Redirect to the album list view after deleting the album

    return render(request, 'label_music_manager/delete_album.html', {'album': album})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True  

class CustomLogoutView(LogoutView):
   next_page = '/accounts/login/'  
