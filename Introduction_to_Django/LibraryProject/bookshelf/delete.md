Python Command

from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()


Expected Output
The book instance is deleted successfully.
