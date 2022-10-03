from . import views
from django.urls import path

urlpatterns = [
    path('', views.Translator_view, name="translator_view")
]