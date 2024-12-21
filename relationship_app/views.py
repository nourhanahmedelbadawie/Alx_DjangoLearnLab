from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library  # Import models if they exist

# Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'list_books.html', {'books': books})

# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model = Library  # Define the model to be used
    template_name = 'library_detail.html'  # Specify the template
    context_object_name = 'library'  # Use 'library' in the template context
