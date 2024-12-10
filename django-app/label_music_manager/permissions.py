from django.http import HttpResponseForbidden

def can_view_album(user, album):
    """Check if the user can view the album."""
    if user.is_superuser:
        return True
    if hasattr(user, 'musicmanageruser'):
        role = user.musicmanageruser.role
        if role == 'artist' and album.artist == user.musicmanageruser.display_name:
            return True
        elif role in ['viewer', 'editor']:
            return True
    return False

def can_edit_album(user, album):
    """Check if the user can edit the album."""
    if user.is_superuser:
        return True
    if hasattr(user, 'musicmanageruser'):
        role = user.musicmanageruser.role
        if role == 'editor':
            return True
        elif role == 'artist' and album.artist == user.musicmanageruser.display_name:
            return True
    return False

def can_delete_album(user, album):
    """Check if the user can delete the album."""
    if user.is_superuser:
        return True
    if hasattr(user, 'musicmanageruser'):
        return user.musicmanageruser.role == 'editor'
    return False
