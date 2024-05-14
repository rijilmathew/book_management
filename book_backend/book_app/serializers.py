# serializers.py

from rest_framework import serializers
from .models import Book, ReadingList, ReadingListBook

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'genre', 'publication_date', 'description']

class ReadingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingList
        fields = ['id', 'user', 'name', 'created_at']

class ReadingListBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingListBook
        fields = ['id', 'order', 'book']
