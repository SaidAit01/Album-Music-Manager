# If you require forms, write them here
#it is used for defining forms that allow users to interact with my application by submitting data 
# These forms are typically used for creating, updating, or validating models or other data inputs. 
# Provides a user-friendly way to create and validate data.

from django import forms
from .models import Album, User, Song

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'release_date', 'description', 'cover_image']  # Add any other relevant fields
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
        help_texts = {
            'title': 'Enter the album title.',
            'artist': 'Specify the artist of the album.',
            'release_date': 'Select the release date.',
            'description': 'Provide a short description of the album.',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title

class UserForm(forms.ModelForm):
    class Meta:
        model = User  # Use your custom User model if applicable
        fields = ['username', 'email', 'is_staff', 'is_active']  # Add fields like roles if applicable
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
        }
        help_texts = {
            'is_staff': 'Indicate if the user is an admin or editor.',
            'is_active': 'Specify if the user account is active.',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Email must be from the 'example.com' domain.")
        return email
















