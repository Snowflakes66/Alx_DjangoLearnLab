
Create Operation
Python Command:

from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()


Expected Output:
The book instance is created successfully.

Retrieve Operation
Python Command:

from bookshelf.models import Book
books = Book.objects.all()
[print(book.title, book.author, book.publication_year) for book in books]


Expected Output:
A list of all book instances in the database, including their title, author, and publication year.

Update Operation
Python Command:

from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()


Expected Output:
The title of the book instance is updated successfully.

Delete Operation
Python Command:

from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()


