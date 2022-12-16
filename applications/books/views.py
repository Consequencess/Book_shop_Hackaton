from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from applications.books.models import Books
from applications.books.serializer import BookSerializer


class BookAPIView(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
