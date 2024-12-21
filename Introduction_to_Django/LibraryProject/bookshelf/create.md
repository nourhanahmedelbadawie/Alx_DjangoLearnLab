# Command to create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected Output: Successfully created the book instance in the database
print(book)  # Should print: 1984 by George Orwell

### Create Operation

**Command:**
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)  # Expected Output: 1984 by George Orwell
