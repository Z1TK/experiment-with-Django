from rest_framework import serializers
from app.author.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'pseudunym', 'description', 'image']

        def validate_name(self, value):
            if not value.strip():
                raise serializers.ValidationError('Name cannot be empty')