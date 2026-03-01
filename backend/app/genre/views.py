from app.genre.models import Genre
from app.genre.serializer import GenreSerializer
from common.base_api_view import BaseView
from django.shortcuts import render


class GenreView(BaseView):
    model = Genre
    serializer_model = GenreSerializer
