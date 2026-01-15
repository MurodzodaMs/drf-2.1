from rest_framework import generics, permissions, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend  # type: ignore

from .models import Book
from .serializer import BookSerializer
from .permissions import IsAuthor

class BookPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5



class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = BookPagination

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    search_fields = ['title']
    filterset_fields = ['genre']


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthor]
