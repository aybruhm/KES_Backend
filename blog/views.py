from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from blog.models import Post


def single_post(request: HttpRequest, slug: str) -> HttpResponse:
    post = Post.objects.get(slug=slug)
    latest_posts = Post.objects.all()[:3]

    context = {
        "post": post,
        "latest_posts": latest_posts
    }

    return render(request, "blog/blog-single.html", context)


def posts(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()

    context = {
        "posts": posts
    }

    return render(request, "blog/blog-grid.html", context)
