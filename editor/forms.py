from django import forms
from editor.models import Post


class ImageUploadForm(forms.Form):
    """Image upload form."""
    name = forms.CharField(max_length=80)
    image = forms.FileField()
