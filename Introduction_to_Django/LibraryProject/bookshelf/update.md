Python Command

from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()


Expected Output
The title of the book instance is updated successfully.

