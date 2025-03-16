from django.db import models



# Define the Author model
class Author(models.Model):
    """
    Represents an author.
    """
    
    # Name field for the author
    name = models.CharField(max_length=100, help_text="The author's name")

# Define the Book model
class Book(models.Model):
    """
    Represents a book.
    """
    
    # Title field for the book
    title = models.CharField(max_length=200, help_text="The book's title")
    
    # Publication year field for the book
    publication_year = models.IntegerField(help_text="The year the book was published")
    
    # Foreign key linking to the Author model
    author = models.ForeignKey(Author, on_delete=models.CASCADE, help_text="The book's author")
