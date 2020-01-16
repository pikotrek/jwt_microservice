from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from books import viewsets

router = DefaultRouter()

router.register(
    'book',
    viewset=viewsets.BookViewSet,
    basename='book'
)

urlpatterns = [
    url(
        '',
        include(
            router.urls
        )
    )
]
