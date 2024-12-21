# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book
from django.shortcuts import render
from .models import Book

from django.shortcuts import render
from .forms import ExampleForm

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Logic for creating a book
        pass
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Logic for editing the book
        pass
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('bookshelf:book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})




def search_books(request):
    user_input = request.GET.get('search', '')
    books = Book.objects.filter(title__icontains=user_input)  # Safe ORM query
    return render(request, 'bookshelf/search_results.html', {'books': books})



def create_book(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data, e.g., save to database
            form.save()
            return redirect('book_list')  # Redirect to a list of books after successful submission
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/create_book.html', {'form': form})
