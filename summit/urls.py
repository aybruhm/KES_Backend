from django.urls import path
from summit import views

app_name = "summit"

urlpatterns = [
    path("", views.summit_page, name="summit_page"),
    path("submit-message/", views.submit_message, name="submit_message")
]
