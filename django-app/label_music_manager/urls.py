# Use this file to specify your subapp's routes
# label_music_manager/urls.py
#DRF routers will handle all api actions 

#The urls.py file in Django is where you define the routing for your application. This file maps URLs to views, 
#allowing you to organize how your application responds to HTTP requests.
# label_music_manager/urls.py
# Use this file to specify your subapp's routes for both HTML views and API views.

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from label_music_manager.api_views import AlbumViewSet, SongViewSet, AlbumTracklistItemViewSet
from label_music_manager import views  # For the views handling HTML pages

# Router for API endpoints
router = DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)
router.register(r'albumtracklistitems', AlbumTracklistItemViewSet)

urlpatterns = [
    # Routes for HTML views
    path('', views.home, name='home'),  # Add this line for the root URL
    path('albums/new/', views.create_album, name='create_album'),  # Create a new album
    path('albums/', views.album_list, name='album_list'),  # List of albums
    path('albums/<int:album_id>/', views.album_detail, name='album_detail'),  # Album details
    path('songs', views.song_list, name='song_list'),  # List of songs
    path('song/<int:song_id>/', views.song_detail, name='song_detail'),  # Song details
   path('albums/<int:album_id>/tracklist/', views.album_tracklist, name='tracklist_items'),  # Album's tracklist
    path('albums/<int:album_id>/edit/', views.edit_album, name='edit_album'),  # Edit an album

    # Routes for API endpoints
    path('api/', include(router.urls)),  # Include API routes from the router
]
