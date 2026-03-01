from app.publisher.models import Publisher
from app.publisher.serializer import (PublisherDetailSerializer,
                                      PublisherSerializer)
from common.base_api_view import BaseDetailView, BaseView
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response


class PublisherView(BaseView):
    model = Publisher
    serializer_model = PublisherSerializer


class PublisherDetailView(BaseDetailView):
    model = Publisher
    serializer_model = PublisherDetailSerializer

    def get(self, request, pk):
        obj = self.model.objects.prefetch_related("titles").get(pk=pk)
        serializer = self.serializer_model(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
