from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
