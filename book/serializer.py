from rest_framework import serializers
from accounts.serializers import RegisterSerializer
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    author = RegisterSerializer(read_only=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'publication_year',
            'genre',
            'author',
        )

    def validate_publication_year(self, value):
        if value > 2026:
            raise serializers.ValidationError(
                'year can not be more than 2026'
            )
        return value

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        return super().create(validated_data)