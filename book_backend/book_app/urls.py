# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, ReadingListViewSet, ReadingListBookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'reading-lists', ReadingListViewSet)
router.register(r'reading-list-books', ReadingListBookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
