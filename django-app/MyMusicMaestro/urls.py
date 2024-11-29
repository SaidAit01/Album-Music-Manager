# You should not edit this file
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from label_music_manager import api_views  # Import your API viewsets



router = DefaultRouter()
router.register(r'albums', api_views.AlbumViewSet)
router.register(r'songs', api_views.SongViewSet)
router.register(r'albumtracklistitems', api_views.AlbumTracklistItemViewSet)

urlpatterns = [
    # Your application URLs (don't include 'label_music_manager.urls' here again)
    path('api/', include(router.urls)),  # Include the API routes
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('datawizard/', include('data_wizard.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('label_music_manager.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
