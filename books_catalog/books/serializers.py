from rest_framework import serializers

from books import models


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Book
        fields = '__all__'
