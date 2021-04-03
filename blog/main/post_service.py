from .models import Post


def post_all():
    return Post.objects.all()
