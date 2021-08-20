from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from summit.models import Message
from blog.models import Post


def summit_page(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by("-date_created")[:3]

    context = {
        "posts": posts
    }
    return render(request, "summit/index.html", context)


def submit_message(request: HttpRequest) -> HttpResponse:
    name = request.POST.get("name")
    email = request.POST.get("email")
    mobile_number = request.POST.get("mobile_number")
    about_you = request.POST.get("describe")

    print(name)
    print(email)
    print(mobile_number)
    print(about_you)

    save_message = Message(
        name=name, email=email, mobile_number=mobile_number, message=about_you
    )
    save_message.save()
    messages.success(request, "Message successfully submitted!")

    return redirect("summit:summit_page")
