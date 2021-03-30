from django.http import JsonResponse
from django.shortcuts import redirect, render


from .forms import PostForm
from .models import Post


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html', {"title": "About company"})


def posts(request):
    posts = Post.objects.all()
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
    posts = Post.objects.all().values('title', 'description', 'content')
    data = list(posts)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
