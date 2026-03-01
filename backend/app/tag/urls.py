from app.tag.views import TagView
from django.urls import path

urlpatterns = [path("tags/", TagView.as_view())]
