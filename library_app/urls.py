# library_app/urls.py
from django.urls import path
from .views import (
    home,
    book_list,
    reader_list,
    borrowed_book_list,
    ReaderDetailView,
    BookCreateView,
    ReaderCreateView,
    BorrowedBookCreateView,
    BookUpdateView,
    ReaderUpdateView,
    BorrowedBookUpdateView,
    BookDeleteView,
    ReaderDeleteView,
    BorrowedBookDeleteView,
)


urlpatterns = [
    path('', home, name='home'),
    path('books/all/', book_list, {'available_only': False}, name='book_list_all'),
    path('books/available/', book_list, {'available_only': True}, name='book_list_available'),
    path('add-book/', BookCreateView.as_view(), name='add_book'),
    path('edit-book/<int:pk>/', BookUpdateView.as_view(), name='edit_book'),
    path('delete-book/<int:pk>/', BookDeleteView.as_view(), name='delete_book'),
    path('readers/', reader_list, name='reader_list'),
    path('add-reader/', ReaderCreateView.as_view(), name='add_reader'),
    path('edit-reader/<int:pk>/', ReaderUpdateView.as_view(), name='edit_reader'),
    path('delete-reader/<int:pk>/', ReaderDeleteView.as_view(), name='delete_reader'),
    path('borrowed-books/', borrowed_book_list, name='borrowed_book_list'),
    path('add-borrowed-book/', BorrowedBookCreateView.as_view(), name='add_borrowed_book'),
    path('edit-borrowed-book/<int:pk>/', BorrowedBookUpdateView.as_view(), name='edit_borrowed_book'),
    path('delete-borrowed-book/<int:pk>/', BorrowedBookDeleteView.as_view(), name='delete_borrowed_book'),
    path('readers/<int:pk>/', ReaderDetailView.as_view(), name='reader_detail')
]