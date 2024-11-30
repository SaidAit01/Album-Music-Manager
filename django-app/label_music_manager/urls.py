# Use this file to specify your subapp's routes
# label_music_manager/urls.py
#DRF routers will handle all api actions 

#The urls.py file in Django is where you define the routing for your application. This file maps URLs to views, 
#allowing you to organize how your application responds to HTTP requests.

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
    path('', views.album_list, name='album_list'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('songs/', views.song_list, name='song_list'),
    path('song/<int:song_id>/', views.song_detail, name='song_detail'),
    path('album/<int:album_id>/tracklist/', views.album_tracklist, name='album_tracklist'),
    path('album/new/', views.create_album, name='create_album'),
    path('album/<int:album_id>/edit/', views.edit_album, name='edit_album'),
    path('user/<int:user_id>/edit/', views.update_user, name='update_user'),
    path('album/<int:album_id>/delete/', views.delete_album, name='delete_album'),
    path('song/new/', views.create_song, name='create_song'),
    path('song/<int:song_id>/edit/', views.edit_song, name='edit_song'),
    path('song/<int:song_id>/delete/', views.delete_song, name='delete_song'), 
    
  
  

    

    # Routes for API
    path('api/', include(router.urls)),
]
