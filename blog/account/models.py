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
    file_path = models.FileField(upload_to='blog/media_content')
