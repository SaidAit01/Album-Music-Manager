# Write your tests here. Use only the Django testing framework.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Album, MusicManagerUser

class AlbumListViewTest(TestCase):
    def setUp(self):
        # Create test users
        self.artist = MusicManagerUser.objects.create_user(
            username='artist_user',
            password='password',
            role='artist',
            display_name='Test Artist'
        )
        self.viewer = MusicManagerUser.objects.create_user(
            username='viewer_user',
            password='password',
            role='viewer',
        )

        # Create test albums
        Album.objects.create(title='Album 1', artist='Test Artist')
        Album.objects.create(title='Album 2', artist='Other Artist')

    def test_artist_sees_own_albums(self):
        self.client.login(username='artist_user', password='password')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Album 1')
        self.assertNotContains(response, 'Album 2')

    def test_viewer_sees_all_albums(self):
        self.client.login(username='viewer_user', password='password')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Album 1')
        self.assertContains(response, 'Album 2')
