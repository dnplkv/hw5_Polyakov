from datetime import datetime

from django.core.cache import cache
from django.db import models
from django.utils.timezone import now

# Create your models here.


class Author(models.Model):
    class Meta:
        db_table = 'tbl_author'
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    name = models.CharField('Имя автора', max_length=100, null=True)
    email = models.EmailField('Email автора', max_length=50, null=True)

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
    title = models.CharField('Заголовок', max_length=80)
    description = models.CharField('Краткое описание', max_length=90)
    content = models.TextField('Статья')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        super().save()
        key = self.__class__.cache_key()
        cache.delete(key)

    @classmethod
    def cache_key(cls):
        dt = datetime.today().strftime('%Y-%m-%d')
        key = f'{dt}'
        return key


class Books(models.Model):
    title = models.CharField('Title', max_length=50)
    author = models.ForeignKey('Author', models.CASCADE, related_name='books')
    category = models.ForeignKey('Category', models.CASCADE, related_name='books', null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField('Name of category', max_length=80, unique=True)

    def __str__(self):
        return self.name


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
    time_exec = models.CharField('Time execution', max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    path = models.CharField('path', max_length=200)
    user_ip = models.CharField('User IP', max_length=20)


class Contacts(models.Model):
    email_to = models.EmailField('Email to holders', max_length=70)
    topic = models.CharField(max_length=150)
    text = models.TextField()


class Rate(models.Model):
    CURRENCY_CHOICES = (
        (1, "USD"),
        (2, "EUR"),
    )

    SOURCE_CHOICES = (
        (1, "PRIVATE_BANK"),
    )

    currency = models.PositiveSmallIntegerField(choices=CURRENCY_CHOICES, db_index=True)
    source = models.PositiveSmallIntegerField(choices=SOURCE_CHOICES)
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sale = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
