from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title", "slug", "image", "date_created", "date_modified"
    ]
    list_display_links = [
        "title", "slug"
    ]
