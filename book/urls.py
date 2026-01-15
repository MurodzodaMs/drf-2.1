from django.urls import path
from .views import BookListCreateAPIView, BookDetailAPIView

urlpatterns = [
    path('', BookListCreateAPIView.as_view()),
    path('<int:pk>/', BookDetailAPIView.as_view()),
]
