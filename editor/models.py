from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField()
    is_share = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)
    # publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.image.storage, self.image.path
        # Delete the model before the file
        super(Post, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)

    def __str__(self):
        # return  ' published by ' + self.publisher.username + 'at' + str(self.date_posted)
        return self.name
