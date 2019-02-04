from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField()
    date_posted = models.DateTimeField(default=timezone.now)
    # publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # return  ' published by ' + self.publisher.username + 'at' + str(self.date_posted)
        return self.name
