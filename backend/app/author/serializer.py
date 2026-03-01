from app.author.models import Author
from app.title.models import Title
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "pseudunym", "description", "image"]

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty")


class AuthorTitles(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ["id", "title", "cover"]


class AuthorDetailSerializer(serializers.ModelSerializer):
    titles = AuthorTitles(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "pseudunym", "description", "image", "titles"]

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty")
