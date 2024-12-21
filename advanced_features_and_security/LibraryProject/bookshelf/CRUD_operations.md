# Step 1: Import the Book model
from bookshelf.models import Book

# Step 2: Create a Book instance
book = Book.objects.create(title="The Great Gatsby", author="F. Scott Fitzgerald", publication_year=1925)

# Step 3: Retrieve the book you created
retrieved_book = Book.objects.get(title="The Great Gatsby")
print(retrieved_book)  # Output: The Great Gatsby by F. Scott Fitzgerald

# Step 4: Update the title of the book
retrieved_book.title = "The Great Gatsby: Revised Edition"
retrieved_book.save()

# Step 5: Verify that the title is updated
updated_book = Book.objects.get(title="The Great Gatsby: Revised Edition")
print(updated_book)  # Output: The Great Gatsby: Revised Edition by F. Scott Fitzgerald

# Step 6: Delete the book instance
retrieved_book.delete()
