from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.utils.safestring import mark_safe
import os


class Post(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='')
    is_share = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)
    # session_id = models.CharField(max_length=100, default='no session')

    def url(self):
        # returns a URL
        return os.path.join('/', settings.MEDIA_URL, os.path.basename(str(self.image)))

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.image.storage, self.image.path
        # Delete the model before the file
        super(Post, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)

    def __str__(self):
        return self.name
