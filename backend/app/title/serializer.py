from rest_framework import serializers
from app.title.models import Title

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ['id', 'title', 'alternative_title', 'description', 'cover', 'type', 'status', 'release_format']

        def validate_title(self, value):
            if not value.strip():
                raise serializers.ValidationError('Title cannot be empty')
            
        def validate_description(self, value):
            if not value.strip():
                raise serializers.ValidationError('Description cannot be empty')
            
        def validate_cover(self, value):
            if not value.strip():
                raise serializers.ValidationError('Cover cannot be empty')