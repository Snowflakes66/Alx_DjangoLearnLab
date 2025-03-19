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
        self.client.force_authenticate(user=self.user)

    def test_filter_books(self):
        url = reverse('api:book-list')
        response = self.client.get(url, {'publication_year': 2020})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        url = reverse('api:book-list')
        response = self.client.get(url, {'search': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        url = reverse('api:book-list')
        response = self.client.get(url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book(self):
        url = reverse('api:book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        new_book = Book.objects.get(title='New Book')
        self.assertEqual(new_book.publication_year, 2021)
        self.assertEqual(new_book.author.id, self.author.id)

    def test_update_book(self):
        url = reverse('api:book-update', args=[self.book.id])
        data = {
            'title': 'Updated Book',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')
        self.assertEqual(self.book.publication_year, 2022)
        self.assertEqual(self.book.author.id, self.author.id)

    def test_delete_book(self):
        url = reverse('api:book-delete', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(title='Test Book')

    def test_list_books(self):
        url = reverse('api:book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
