from rest_framework import serializers
from .models import Book, Author
from datetime import date

# Define the BookSerializer class
class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    """
    
    # Validate publication year to ensure it's not in the future
    def validate_publication_year(self, value):
        """
        Validate the publication year to ensure it's not greater than the current year.
        """
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be greater than the current year")
        return value
    
    class Meta:
        # Specify the Book model
        model = Book
        
        # Specify the fields to serialize
        fields = ['id', 'title', 'publication_year', 'author']

# Define the AuthorSerializer class
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    """
    
    # Include a nested BookSerializer to serialize related books
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        # Specify the Author model
        model = Author
        
        # Specify the fields to serialize
        fields = ['id', 'name','books']

