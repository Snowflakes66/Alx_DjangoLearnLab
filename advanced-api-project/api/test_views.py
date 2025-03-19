from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(name='testauthor')
        self.book = Book.objects.create(title='Test Book', publication_year=2020, author=self.author)

    def test_create_book(self):
        data = {'title': 'New Book', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.post(reverse('api:book-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_read_book(self):
        response = self.client.get(reverse('api:book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_update_book(self):
        data = {'title': 'Updated Book', 'publication_year': 2022, 'author': self.author.id}
        response = self.client.put(reverse('api:book-update', args=[self.book.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        response = self.client.delete(reverse('api:book-delete', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        response = self.client.get(reverse('api:book-list'), {'author': self.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(reverse('api:book-list'), {'search': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        response = self.client.get(reverse('api:book-list'), {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

