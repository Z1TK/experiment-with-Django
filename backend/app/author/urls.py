from app.author.views import AuthorDetailSerializer, AuthorView
from django.urls import path

urlpatterns = [
    path("authors/", AuthorView.as_view()),
    path("authors/<uuid:pk>", AuthorDetailSerializer.as_view()),
]
