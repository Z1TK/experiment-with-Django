from app.publisher.views import PublisherDetailView, PublisherView
from django.urls import path

urlpatterns = [
    path("publishers/", PublisherView.as_view()),
    path("publishers/<uuid:pk>", PublisherDetailView.as_view()),
]
