from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Library, Book  # Import models if they exist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm  # Assuming you have a BookForm
from django.contrib.auth.decorators import permission_required


# Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view for library detail
class LibraryDetailView(DetailView):
    model = Library  # Specify the model
    template_name = 'relationship_app/library_detail.html'  # Path to the template
    context_object_name = 'library'  # Name used in the template context


# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Role-checking decorator
def check_role(role):
    def decorator(user):
        return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role
    return decorator


# Views restricted by role
@user_passes_test(check_role('Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'role': 'Admin'})


@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {'role': 'Librarian'})


@user_passes_test(check_role('Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'role': 'Member'})


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Replace with your book list view name
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Replace with your book list view name
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Replace with your book list view name
    return render(request, 'relationship_app/delete_book.html', {'book': book})
