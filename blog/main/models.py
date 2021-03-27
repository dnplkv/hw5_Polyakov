from django.db import models
from django.utils.timezone import now

# Create your models here.


class User(models.Model):
    class Meta:
        db_table = 'tbl_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    name = models.CharField('Имя пользователя', max_length=100)
    email = models.CharField('Email пользователя', max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        db_table = 'tbl_post'
    title = models.CharField('Заголовок', max_length=40)
    description = models.CharField('Краткое описание', max_length=90)
    content = models.TextField('Статья')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return self.title
