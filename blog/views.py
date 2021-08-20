from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def single_post(request: HttpRequest) -> HttpResponse:

    context = {}

    return render(request, "blog/blog-single.html", context)


def posts(request: HttpRequest, slug: str) -> HttpResponse:

    context = {}

    return render(request, "blog/blog-grid.html", context)
