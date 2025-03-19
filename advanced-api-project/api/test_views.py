
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from .serializers import BookSerializer

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.book1 = Book.objects.create(title='Book 1', publication_year=2020)
        self.book2 = Book.objects.create(title='Book 2', publication_year=2021)

    def test_get_all_books(self):
        response = self.client.get(reverse('book-list'))
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_book(self):
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book1.pk}))
        book = Book.objects.get(pk=self.book1.pk)
        serializer = BookSerializer(book)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_book(self):
        response = self.client.get(reverse('book-detail', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_book(self):
        data = {'title': 'New Book', 'publication_year': 2022}
        response = self.client.post(reverse('book-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_invalid_book(self):
        data = {'title': '', 'publication_year': 2022}
        response = self.client.post(reverse('book-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_valid_book(self):
        data = {'title': 'Updated Book', 'publication_year': 2022}
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book1.pk}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=self.book1.pk).title, 'Updated Book')

    def test_update_invalid_book(self):
        data = {'title': '', 'publication_year': 2022}
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book1.pk}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_book(self):
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_invalid_book(self):
        response = self.client.delete(reverse('book-detail', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

