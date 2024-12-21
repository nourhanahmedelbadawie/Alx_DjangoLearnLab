from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library,Book # Import models if they exist
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Function-based view for listing all books

def list_books(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'relationship_app/list_books.html', {'books': books})


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
            username = form.cleaned_data.get('username')
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
