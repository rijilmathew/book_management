from django.db import models
from authentication.models import CustomUser

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField(blank=True, null=True)


class ReadingList(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class ReadingListOrder(models.Model):
    reading_list = models.OneToOneField(ReadingList, on_delete=models.CASCADE, related_name='order')
    books = models.ManyToManyField(Book, through='ReadingListBook')
    
class ReadingListBook(models.Model):
    order = models.PositiveIntegerField()
    reading_list_order = models.ForeignKey(ReadingListOrder, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)