from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "data_created", "author")

admin.site.register(Post, PostAdmin)