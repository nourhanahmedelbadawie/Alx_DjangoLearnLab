from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library,Book # Import models if they exist

# Function-based view for listing all books

def list_books(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library  # Specify the model
    template_name = 'relationship_app/library_detail.html'  # Path to the template
    context_object_name = 'library'  # Name used in the template context