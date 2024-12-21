from django.urls import path
from .views import  list_books , LibraryDetailView# This is the missing import
from django.contrib.auth import views as views
from .views import admin_view, librarian_view, member_view , edit_book , delete_book , add_book
from . import views

urlpatterns = [
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('login/', views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),  # Link the 'register' URL to the 'register' view ,
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    path('books/add/', add_book, name='add_book'),
    path('books/<int:book_id>/edit_book/', edit_book, name='edit_book'),
    path('books/<int:book_id>/delete_book/', delete_book, name='delete_book'),
    path('books/', list_books, name='list_books'),

]
