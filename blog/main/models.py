from django.db import models
from django.utils.timezone import now

# Create your models here.


class Author(models.Model):
    class Meta:
        db_table = 'tbl_author'
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    name = models.CharField('Имя автора', max_length=100)
    email = models.EmailField('Email автора', max_length=50)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    email_to = models.EmailField('Email подписчика', max_length=50)
    author_id = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.email_to


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


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


class Log(models.Model):
    utm = models.CharField('utm mark', max_length=50)
    time_exec = models.CharField('time execution', max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    path = models.CharField('path', max_length=200)
    ip_address = models.GenericIPAddressField()
