from time import time

from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from faker import Faker

from .forms import CommentForm, PostForm, SubscriberForm
from .models import Author, Books, Category, Post, Subscriber
from .notify_service import notify
from .post_service import post_all, post_find
from .subscribe_service import get_author_name, subscribe
from .tasks import email_send_to_subs, notify_async


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html', {"title": "About company"})


def posts(request):
    posts = post_all()
    return render(request, 'main/posts_all.html', {"title": "Posts", "posts": posts})


def posts_create(request):
    # template
    # {% url 'posts_show' post_id=post.id %}

    # view
    # reverse('posts_show') => posts/update/<int:post_id>
    # reverse('posts_create') => /posts/create
    # print(reverse('posts_show', args=[1]))

    err_custom = ""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_all')
        else:
            err_custom = "Error on save Post"
    else:
        form = PostForm()
    context = {
        'form': form,
        'err_my': err_custom
    }
    return render(request, 'main/posts_create.html', context=context)


def posts_update(request, post_id):
    err = ""
    pst = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(instance=pst, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_all')
        else:
            err = "Error on update Post"
    else:
        form = PostForm(instance=pst)
    context = {
        'form': form,
        'err_my': err
    }
    return render(request, 'main/posts_update.html', context=context)


def posts_show(request, post_id):
    pst = post_find(post_id)
    comments = pst.comments.filter()
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = pst
            # Save the comment to the database
            new_comment.save()
            return redirect('posts_show', post_id=post_id)
    else:
        comment_form = CommentForm()
    return render(request, 'main/posts_show.html', {"title": pst.title,
                                                    "pst": pst,
                                                    "comments": comments,
                                                    "new_comment": new_comment,
                                                    "comment_form": comment_form,
                                                    })


def subscribers_new(request):
    err = ""
    subscribe_success = False
    email_to = request.POST.get('email_to')

    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('subscribers_all')
            subscribe_success = True
        else:
            err = "Error"
    else:
        form = SubscriberForm()

    if subscribe_success:
        author_name = get_author_name(request)
        notify_async.delay(email_to, author_name)

        return redirect('subscribers_all')

    context = {
        'form': form,
        'err': err
    }
    # author_id = request.GET["author_id"]
    # email_to = request.GET["email_to"]
    #
    # subscribe_process(author_id, email_to)

    return render(request, 'main/subscriber_new.html', context=context)


def subscribers_all(request):
    all_val = Subscriber.objects.all()
    # all.delete()
    return render(request, 'main/subscribers.html', {'title': 'All subs', 'subscribers': all_val})


def authors_new(request):
    faker = Faker()
    Author(name=faker.name(), email=faker.email()).save()
    # all = Author.objects.all().values('name', 'email')
    # all.delete()
    return HttpResponseRedirect(reverse('authors_all'))
    # return redirect('authors_all')


def authors_all(request):
    all_val = Author.objects.all().prefetch_related('books')
    # all.delete()
    return render(request, 'main/authors.html', {'title': 'Authors', 'authors': all_val})


def books_all(request):
    books = Books.objects.all().only("title", "category").select_related("category")
    context = {'books': books}
    return render(request, 'main/books.html', context)


def categories_all(request):
    categories = Category.objects.only("name").distinct().prefetch_related('books')
    context = {'categories': categories}
    return render(request, 'main/categories.html', context)


def api_authors_new(request):
    faker = Faker()
    Author(name=faker.name(), email=faker.email()).save()
    all_val = Author.objects.all().values('name', 'email')
    return JsonResponse(list(all_val), safe=False)


def api_authors_all(request):
    faker = Faker()
    Author(name=faker.name(), email=faker.email()).save()
    all_val = Author.objects.all().values('id', 'name', 'email')
    return JsonResponse(list(all_val), safe=False)


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


def api_posts_show(request, post_id):
    pst = post_find(post_id)
    dict_obj = model_to_dict(pst)
    return JsonResponse(dict_obj, safe=False)


def api_subscribers_all(request):
    all_val = Subscriber.objects.all().values('email_to', 'author_id')
    data = list(all_val)
    return JsonResponse(data, safe=False)


def subscribe_process(author_id, email_to):
    subscribe(author_id, email_to)
    notify(email_to)


def email_to_all_subs(request):
    st = time()
    print("*** START ***")
    email_send_to_subs.delay()
    time_exec = time() - st
    print(f"*** FINISH *** {time_exec}")
    return redirect('home_page')
