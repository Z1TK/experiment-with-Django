from app.author.models import Author
from app.genre.models import Genre
from app.publisher.models import Publisher
from app.tag.models import Tag
from app.title.models import Title
from rest_framework import serializers


class TitleAuthor(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]


class TitlePublisher(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["id", "name"]


class TitleTag(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class TitleGenre(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]

class TitleSerializer(serializers.ModelSerializer):
    author = TitleAuthor()
    publisher = TitlePublisher()
    genres = TitleGenre(many=True)
    tags = TitleTag(many=True)

    class Meta:
        model = Title
        fields = [
            "id",
            "title",
            "alternative_title",
            "description",
            "cover",
            "author",
            "publisher",
            "type",
            "status",
            "release_format",
            "genres",
            "tags",
        ]

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty")

    def validate_description(self, value):
        if not value.strip():
            raise serializers.ValidationError("Description cannot be empty")

    def validate_cover(self, value):
        if not value.strip():
            raise serializers.ValidationError("Cover cannot be empty")
