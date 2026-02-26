from rest_framework import serializers
from app.publisher.models import Publisher

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'another_name', 'description', 'image']

        def validate_name(self, value):
            if not value.strip():
                raise serializers.ValidationError('Name cannot be empty')