from django import forms
from editor.models import Post
from . import choices


class ImageUploadForm(forms.Form):
    """Image upload form."""
    name = forms.CharField(max_length=80)
    image = forms.FileField()


class RadioEditForm(forms.Form):
    """Choose which kind of edit form"""
    edit_choice = forms.ChoiceField(choices=choices.EDIT_CHOICES, widget=forms.RadioSelect)