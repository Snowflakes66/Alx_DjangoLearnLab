# advanced-api-project/api/views.py
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]



# advanced-api-project/api/views.py
class BookCreateView(generics.CreateAPIView):
    # ...
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BookUpdateView(generics.UpdateAPIView):
    # ...
    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


# advanced-api-project/api/views.py
from rest_framework import permissions

class BookListView(generics.ListAPIView):
    # ...
    permission_classes = [permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    # ...
    permission_classes = [permissions.AllowAny]



