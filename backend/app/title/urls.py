from app.title.views import TitleView, TitleDetailView
from django.urls import path

urlpatterns = [
    path("titles/", TitleView.as_view()),
    path("titles/<int:pk>", TitleDetailView.as_view())
]
