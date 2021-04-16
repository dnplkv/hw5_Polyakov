from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from .models import Author, Subscriber


def subscribe(author_id, email_to):
    try:
        Subscriber.objects.get(email_to=email_to, author=author_id)
    except ObjectDoesNotExist:
        subscriber = Subscriber(email_to=email_to, author=author_id)
        subscriber.save()


def get_author_name(request):
    if request.method == "POST":
        author_id = request.POST["author_id"]
    else:
        author_id = request.GET["author_id"]
    author = get_object_or_404(Author, pk=author_id)
    return author.name
