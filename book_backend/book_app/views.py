# views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Book, ReadingList, ReadingListOrder, ReadingListBook
from .serializers import BookSerializer, ReadingListSerializer, ReadingListBookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ReadingListViewSet(viewsets.ModelViewSet):
    queryset = ReadingList.objects.all()
    serializer_class = ReadingListSerializer

class ReadingListBookViewSet(viewsets.ModelViewSet):
    queryset = ReadingListBook.objects.all()
    serializer_class = ReadingListBookSerializer

    def create(self, request, *args, **kwargs):
        # Validate data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Create or update ReadingListOrder
        reading_list = serializer.validated_data['reading_list_order']
        book = serializer.validated_data['book']
        order = serializer.validated_data['order']
        
        reading_list_order, created = ReadingListOrder.objects.get_or_create(reading_list=reading_list)
        ReadingListBook.objects.create(reading_list_order=reading_list_order, book=book, order=order)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
