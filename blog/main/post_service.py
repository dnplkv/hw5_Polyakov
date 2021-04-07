from .models import Post


def post_all():
    return Post.objects.all()


def post_find(post_id: int) -> Post:
    return Post.objects.get(id=post_id)
