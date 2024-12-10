from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from label_music_manager.api_views import AlbumViewSet, SongViewSet, AlbumTracklistItemViewSet
from label_music_manager import views
from .views import CustomLoginView, CustomLogoutView

# Router for API endpoints
router = DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)
router.register(r'tracklist', AlbumTracklistItemViewSet)

urlpatterns = [
    # Root route redirects to /albums/
    path('', lambda request: redirect('album_list'), name='home'),

    # Specific routes for edit and delete
    path('albums/<int:album_id>/edit/', views.edit_album, name='edit_album'),
    path('albums/<int:album_id>/delete/', views.delete_album, name='delete_album'),

    # General routes
    path('albums/<int:album_id>/<slug:slug>/', views.album_detail, name='album_detail_with_slug'),
    path('albums/<int:album_id>/', views.album_detail, name='album_detail'),

    # Album list
    path('albums/', views.album_list, name='album_list'),
    path('albums/new/', views.create_album, name='create_album'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    

    # Routes for API endpoints
    path('api/', include(router.urls)),
]
