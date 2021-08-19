from django.shortcuts import redirect, render, redirect


def summit_page(request):
    return render(request, "summit/index.html")


def submit_message(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    mobile_number = request.POST.get("mobile_number")
    about_you = request.POST.get("describe")

    print(name)
    print(email)
    print(mobile_number)
    print(about_you)

    return redirect("summit:summit_page")
