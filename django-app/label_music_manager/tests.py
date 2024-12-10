from django.test import SimpleTestCase, TestCase
from django.core.exceptions import ValidationError
from label_music_manager.models import Album, Song, AlbumTracklistItem, MusicManagerUser
from label_music_manager.forms import AlbumForm
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from label_music_manager.views import album_list, create_album


class ModelTests(TestCase):
    def setUp(self):
        # Create a user
        self.user = MusicManagerUser.objects.create_user(
            username="testuser", password="password", role="artist", display_name="Test Artist"
        )
        
        # Create album
        self.album = Album.objects.create(
            title="Test Album",
            artist="Test Artist",
            price=10.99,
            format="CD",
            release_date="2024-12-01",
        )
        
        # Create song
        self.song = Song.objects.create(title="Test Song", running_time=120)

    def test_album_price_validation(self):
        self.album.price = -5  # Invalid price
        with self.assertRaises(ValidationError):
            self.album.full_clean()

    def test_song_running_time(self):
        self.song.running_time = 5  # Invalid running time
        with self.assertRaises(ValidationError):
            self.song.full_clean()

    def test_album_tracklist_relationship(self):
        track_item = AlbumTracklistItem.objects.create(album=self.album, song=self.song, position=1)
        self.assertEqual(track_item.album.title, "Test Album")
        self.assertEqual(track_item.song.title, "Test Song")


class PermissionTests(TestCase):
    def setUp(self):
        # Create users with roles
        self.artist = MusicManagerUser.objects.create_user(username="artist", password="password", role="artist")
        self.editor = MusicManagerUser.objects.create_user(username="editor", password="password", role="editor")
        self.viewer = MusicManagerUser.objects.create_user(username="viewer", password="password", role="viewer")

        # Create album
        self.album = Album.objects.create(title="Album 1", artist="artist", price=9.99, format="CD", release_date="2024-12-01")

def test_artist_permissions(self):
    self.album.artist = "Test Artist"
    self.album.save()
    self.artist.display_name = "Test Artist"
    self.artist.save()
    self.assertTrue(self.artist.can_view("Test Artist"))

    def test_editor_permissions(self):
        self.assertTrue(self.editor.can_edit())
        self.assertTrue(self.editor.can_view("artist"))

    def test_viewer_permissions(self):
        self.assertTrue(self.viewer.can_view("artist"))
        self.assertFalse(self.viewer.can_edit())
    

class ViewTests(TestCase):
    def setUp(self):
        # Create user
        self.editor = MusicManagerUser.objects.create_user(username="editor", password="password", role="editor")

        # Create album
        self.album = Album.objects.create(title="Test Album", artist="Test Artist", price=1.99, format="CD", release_date="2024-12-10")

def test_album_list_view(self):
    self.client.login(username="editor", password="password")
    response = self.client.get(reverse("album_list"))
    print(response.url) 
    self.assertEqual(response.status_code, 200)

def test_album_detail_view(self):
    self.client.login(username="editor", password="password")
    response = self.client.get(reverse("album_detail", args=[self.album.id]))
    print(response.url) 
    self.assertEqual(response.status_code, 200)

from django.test import TestCase
from django.contrib.admin.sites import site
from label_music_manager.models import Album, Song, AlbumTracklistItem, MusicManagerUser
from label_music_manager.admin import AlbumAdmin

class AdminTests(TestCase):
    def test_album_registered_in_admin(self):
        self.assertIn(Album, site._registry)
        self.assertIsInstance(site._registry[Album], AlbumAdmin)

    def test_song_registered_in_admin(self):
        self.assertIn(Song, site._registry)

    def test_album_tracklist_item_registered_in_admin(self):
        self.assertIn(AlbumTracklistItem, site._registry)

    def test_music_manager_user_registered_in_admin(self):
        self.assertIn(MusicManagerUser, site._registry)

class AlbumFormTests(TestCase):
    def setUp(self):
        self.song = Song.objects.create(title="Test Song", running_time=120)

    def test_form_valid_data(self):
        form = AlbumForm(data={
            "title": "Test Album",
            "artist": "Test Artist",
            "price": 10,
            "release_date": "2025-01-01",
        }, files={})
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = AlbumForm(data={
            "title": "",  # Missing title
            "artist": "Test Artist",
            "price": 10,
            "release_date": "2024-12-11",
        })
        self.assertFalse(form.is_valid())


class URLTests(SimpleTestCase):
    def test_album_list_url(self):
        url = reverse("album_list")
        self.assertEqual(resolve(url).func, album_list)

    def test_create_album_url(self):
        url = reverse("create_album")
        self.assertEqual(resolve(url).func, create_album)

class APIViewsTests(TestCase):
    def setUp(self):
        # Use the custom manager to create users with roles
        User = get_user_model()
        self.user = User.objects.create_user(
            username="editor_user",
            password="password",
            role="editor",
            display_name="Editor User"
        )

        self.album = Album.objects.create(
            title="Test Album",
            artist="Test Artist",
            price=10.99,
            format="Degital",
            release_date="2023-12-04"
        )


   