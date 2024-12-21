### Retrieve Operation

**Command:**
```python
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book)  # Expected Output: 1984 by George Orwell
