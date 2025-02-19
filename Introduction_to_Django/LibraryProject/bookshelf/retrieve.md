["Book.objects.get", "1984"]

Python Command

from bookshelf.models import Book
books = Book.objects.all()
[print(book.title, book.author, book.publication_year) for book in books]


Expected Output
A list of all book instances in the database, including their title, author, and publication year.

