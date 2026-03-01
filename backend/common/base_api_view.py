from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class BaseView(APIView):
    model = None
    serializer_model = None

    def get(self, request):
        obj = self.model.objects.all()
        serializer = self.serializer_model(obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_model(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BaseDetailView(APIView):
    model = None
    serializer_model = None

    def put(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_model(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
