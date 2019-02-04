from django import forms
from editor.models import Post

# class UploadImgForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.ImageField()


class ImageUploadForm(forms.Form):
    """Image upload form."""
    name = forms.CharField(max_length=80)
    image = forms.FileField()
    # class Meta:
    #     model = Post
    #     fields = ('D')