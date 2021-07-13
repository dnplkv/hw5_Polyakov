import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField('Email address', blank=False, null=False, unique=True)
    confirmation_token = models.UUIDField(default=uuid.uuid4)


def user_ava_upload(instance, filename):
    return f'{instance.user_id}/{filename}'


class Ava(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.FileField(upload_to=user_ava_upload)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.FileField(null=True, blank=True, upload_to=user_ava_upload)

    def __str__(self):
        return str(self.user)
