from django.shortcuts import render
from .models import Post
from django.views import generic
# Create your views here.

class Blog_view(generic.DetailView):
    model = Post
    template_name = "blog.html"


class About_view(generic.TemplateView):
    template_name = "about.html"


class Post_list(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("data_created")
    template_name = "index.html"