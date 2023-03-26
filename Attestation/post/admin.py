from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author']
    list_display_links = ['author']
    list_filter = ['creation_date']
