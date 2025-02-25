from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = 'J.K. Rowling'
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
print("Books by J.K. Rowling:")
for book in books:
    print(book.title)

# List all books in a library
library_name = 'New York Public Library'
library = Library.objects.get(name=library_name)
books = library.books.all()
print("\nBooks in New York Public Library:")
for book in books:
    print(book.title)

# Retrieve the librarian for a library
library = Library.objects.get(name='New York Public Library')
librarian = Librarian.objects.get(library=library)
print("\nLibrarian for New York Public Library:")
print(librarian.name)
