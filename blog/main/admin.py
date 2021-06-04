from account.models import User
from django.contrib import admin

from .models import Author, Comment, Log, Post


admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Log)
admin.site.register(User)
