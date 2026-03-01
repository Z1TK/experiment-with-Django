from app.genre.views import GenreView
from django.urls import path

urlpatterns = [path("genres/", GenreView.as_view())]
