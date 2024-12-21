
#### **Delete Operation (`delete.md`)**

Command: Delete the book instance and confirm its deletion by attempting to retrieve all books.

```python
# Delete the book instance
retrieved_book.delete()

# Attempt to retrieve the deleted book
try:
    deleted_book = Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("The book was successfully deleted.")  # Expected Output: The book was successfully deleted.

### Delete Operation

**Command:**
```python
retrieved_book.delete()

# Attempt to retrieve the deleted book
try:
    deleted_book = Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("The book was successfully deleted.")
