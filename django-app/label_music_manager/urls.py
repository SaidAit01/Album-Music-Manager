from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from label_music_manager.api_views import AlbumViewSet, SongViewSet, AlbumTracklistItemViewSet
from label_music_manager import views
from .views import CustomLoginView, CustomLogoutView


router = DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)
router.register(r'tracklist', AlbumTracklistItemViewSet)

urlpatterns = [

    path('api/', include(router.urls)),
    path('', lambda request: redirect('album_list'), name='home'),


    path('albums/<int:album_id>/edit/', views.edit_album, name='edit_album'),
    path('albums/<int:album_id>/delete/', views.delete_album, name='delete_album'),

    
    path('albums/<int:album_id>/<slug:slug>/', views.album_detail, name='album_detail_with_slug'),
    path('albums/<int:album_id>/', views.album_detail, name='album_detail'),

    
    path('albums/', views.album_list, name='album_list'),
    path('albums/new/', views.create_album, name='create_album'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    
   





]
