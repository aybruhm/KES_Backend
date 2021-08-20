from django.urls import path
from blog import views


app_name = "blog"

urlpatterns = [
    path("", views.posts, name="posts"),
    path("<slug:slug>/",  views.single_post, name="post")
]
