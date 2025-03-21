# advanced-api-project/api/urls.py
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)
app_name = 'api'
urlpatterns = [
    path('books/', BookListView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
    path('books/create/', BookCreateView.as_view()),
    path('books/update/<int:pk>/', BookUpdateView.as_view()),
    path('books/delete/<int:pk>/', BookDeleteView.as_view()),
]