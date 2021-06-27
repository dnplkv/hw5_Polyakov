from account.models import Ava, User
from django.contrib import admin

from .models import Author, Comment, Log, Post, Rate


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'created',
    ]

    list_filter = [
        'title',
        'created',
    ]

    readonly_fields = ['title', 'content']

    def get_readonly_fields(self, request, obj=None):
        request.user.groups.filter(name='managers')
        if request.user.is_superuser:
            return ()
        return super().get_readonly_fields(request, obj)

    # def has_delete_permission(self, request, obj=None):
    #     return request.user.is_superuser


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Log)
admin.site.register(User)

admin.site.register(Ava)
admin.site.register(Rate)
