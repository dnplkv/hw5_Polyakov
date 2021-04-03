from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm, SubscriberForm
from .models import Author
from .notify_service import notify
from .post_service import post_all
from .subscribe_service import subscribe


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html', {"title": "About company"})


def posts(request):
    posts = post_all()
    return render(request, 'main/posts.html', {"title": "Посты", "posts": posts})


def posts_create(request):
    err = ""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            err = "Error on save Post"
    else:
        form = PostForm()
    context = {
        'from': form,
        'err': err
    }
    return render(request, 'main/posts_create.html', context=context)


def json_posts(request):
    posts_cont = post_all().values('title', 'description', 'content')
    data = list(posts_cont)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def api_subscribe(request):
    author_id = request.GET["author_id"]
    email_to = request.GET["email_to"]

    get_object_or_404(Author, pk=author_id)

    subscribe_process(author_id, email_to)

    data = {"author_id": author_id}
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def posts_subscribe(request):
    err = ""
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main/posts_subscribe.html')
        else:
            err = "Error"
    else:
        form = SubscriberForm()
    context = {
        'from': form,
        'err': err
    }
    # author_id = request.GET["author_id"]
    # email_to = request.GET["email_to"]
    #
    # subscribe_process(author_id, email_to)

    return render(request, 'main/posts_subscribe.html', context=context)


def subscribe_process(author_id, email_to):
    subscribe(author_id, email_to)
    notify(email_to)
