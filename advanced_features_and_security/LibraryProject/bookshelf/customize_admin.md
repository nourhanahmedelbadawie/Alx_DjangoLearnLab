# Customize Admin Interface for Book Model
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Display the following fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filter options for the publication year
    list_filter = ('publication_year',)
    
    # Enable search functionality for title and author
    search_fields = ('title', 'author')

# Register the Book model with the custom BookAdmin
admin.site.register(Book, BookAdmin)

## Steps to Customize the Admin:

### 1. Register the `Book` Model with the Django Admin

In `bookshelf/admin.py`, register the `Book` model to enable it in the Django admin interface:

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
