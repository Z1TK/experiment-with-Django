from app.publisher.models import Publisher
from app.title.models import Title
from rest_framework import serializers


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["id", "name", "another_name", "description", "image"]

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty")


class PublisherTitles(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ["id", "title", "cover"]


class PublisherDetailSerializer(serializers.ModelSerializer):
    titles = PublisherTitles(many=True, read_only=True)

    class Meta:
        model = Publisher
        fields = ["id", "name", "pseudunym", "description", "image", "titles"]

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty")
