from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>', views.Blog_view.as_view(), name="blog_view"),
    path('about/', views.About_view.as_view(), name="about_view"),
    path('', views.Post_list.as_view(), name="home_view")
]

