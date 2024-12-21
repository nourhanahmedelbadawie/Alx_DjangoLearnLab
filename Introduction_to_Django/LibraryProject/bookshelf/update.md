### Update Operation

**Command:**
```python
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print(updated_book)  # Expected Output: Nineteen Eighty-Four by George Orwell
