from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from books import models, serializers


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return models.Book.objects.prefetch_related('authors')
