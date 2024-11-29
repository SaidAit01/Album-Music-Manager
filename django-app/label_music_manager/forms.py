# If you require forms, write them here
#it is used for defining forms that allow users to interact with my application by submitting data 
# These forms are typically used for creating, updating, or validating models or other data inputs. 
# Provides a user-friendly way to create and validate data.

# forms.py
from django import forms
from .models import Album, User

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


