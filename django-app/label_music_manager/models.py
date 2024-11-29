from django.db import models
from django.forms import ValidationError
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser, Group, Permission


class Album(models.Model):
    FORMAT_CHOICES = [
        ('CD', 'CD'),
        ('Vinyl', 'Vinyl'),
        ('Digital', 'Digital'),
    ]
    name = models.CharField(max_length=255, default="Default Name")
    title = models.CharField(max_length=255)  # Required album title
    description = models.TextField(blank=True, null=True)  # Optional description
    artist = models.CharField(max_length=255)  # Artist name
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price with constraints
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES)  # Format (CD/Vinyl/Digital)
    release_date = models.DateField()  # Release date of the album
    slug = models.SlugField(unique=True, blank=True)  # Slug for SEO-friendly URLs
    cover_image = models.ImageField(blank=True, null=True, default='default_cover.jpg')  # Optional cover image

    def save(self, *args, **kwargs):
        # Auto-generate slug from title if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(price__gte=0), name="price_gte_0"),  # Price >= 0
            models.CheckConstraint(check=models.Q(price__lte=999.99), name="price_lte_999_99"),  # Price <= 999.99
        ]


class Song(models.Model):
    title = models.CharField(max_length=200)  # Required song title
    running_time = models.PositiveIntegerField()  # Length of the song in seconds
    albums = models.ManyToManyField(
        'Album',
        through='AlbumTracklistItem',
        related_name='songs'  # Allows reverse lookup from Album to Song
    )
    position = models.PositiveIntegerField(null=True, blank=True)  # Position in album (optional)

    def clean(self):
        # Validate that running time is at least 10 seconds
        if self.running_time < 10:
            raise ValidationError('Running time must be at least 10 seconds.')

    def __str__(self):
        return self.title


class AlbumTracklistItem(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracklist')  # Reference to Album
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='tracklist_items')  # Reference to Song
    position = models.PositiveIntegerField()  # Position in the album's tracklist

    class Meta:
        unique_together = ['album', 'position']  # A song's position must be unique within an album
        ordering = ['position']  # Default ordering by position

    def __str__(self):
        return f"{self.album.title} - {self.song.title} (Position {self.position})"


class MusicManagerUser(AbstractUser):
    # Extending the default Django User model
    ROLE_CHOICES = [
        ('artist', 'Artist'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)  # User's role

    # Custom related names for groups and permissions to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name="custom_music_manager_users",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_music_manager_users",
        blank=True,
    )

    def __str__(self):
        return self.username
