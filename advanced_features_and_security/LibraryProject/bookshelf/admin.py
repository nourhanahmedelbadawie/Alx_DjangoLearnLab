# bookshelf/admin.py
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for the publication year
    list_filter = ('publication_year',)
    
    # Enable search functionality for title and author fields
    search_fields = ('title', 'author')

# Register the Book model with the custom BookAdmin
admin.site.register(Book, BookAdmin)
