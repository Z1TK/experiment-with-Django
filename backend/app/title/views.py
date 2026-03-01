from app.title.models import Title
from app.title.serializer import TitleSerializer
from common.base_api_view import BaseDetailView, BaseView
from rest_framework import status
from rest_framework.response import Response


class TitleView(BaseView):
    model = Title
    serializer_model = TitleSerializer


class TitleDetailView(BaseDetailView):
    model = Title
    serializer_model = TitleSerializer

    def get(self, request, pk):
        obj = self.model.objects.select_related('author', 'publisher').prefetch_related('genres', 'tags').get(pk=pk)
        serializer = self.serializer_model(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)