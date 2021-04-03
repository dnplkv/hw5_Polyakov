from django.db import models
from django.utils.timezone import now

# Create your models here.


class Author(models.Model):
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
    name = models.CharField('Имя автора', max_length=100)
    email = models.EmailField('Email автора', max_length=50)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    email_to = models.EmailField('Email подписчика')
    author_id = models.ForeignKey('Author', on_delete=models.CASCADE)

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
