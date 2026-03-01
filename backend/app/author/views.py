from app.author.models import Author
from app.author.serializer import AuthorDetailSerializer, AuthorSerializer
from common.base_api_view import BaseDetailView, BaseView
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response


class AuthorView(BaseView):
    model = Author
    serializer_model = AuthorSerializer


class AuthorDetailView(BaseDetailView):
    model = Author
    serializer_model = AuthorDetailSerializer

    def get(self, request, pk):
        obj = self.model.objects.prefetch_related("titles").get(pk=pk)
        serializer = self.serializer_model(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
