# label_music_manager/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from label_music_manager.api_views import AlbumViewSet, SongViewSet, AlbumTracklistItemViewSet
from label_music_manager import views

# Router for API endpoints
router = DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)
router.register(r'albumtracklistitems', AlbumTracklistItemViewSet)

urlpatterns = [
    # Routes for HTML views
    path('', views.home, name='home'),
    path('albums/new/', views.create_album, name='create_album'),
    path('albums/', views.album_list, name='album_list'),
    path('albums/<int:album_id>/', views.album_detail, name='album_detail'),
    path('songs', views.song_list, name='song_list'),
    path('song/<int:song_id>/', views.song_detail, name='song_detail'),
    path('albums/<int:album_id>/tracklist/', views.album_tracklist, name='tracklist_items'),
    path('albums/<int:album_id>/edit/', views.edit_album, name='edit_album'),
    path('albums/<int:album_id>/delete/', views.delete_album, name='delete_album'),

    # Routes for API endpoints
    path('api/', include(router.urls)),
]
