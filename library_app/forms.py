from django import forms
from .models import Book, Reader, BorrowedBook

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'genre', 'publisher', 'is_available']

class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['first_name', 'last_name', 'phone_number', 'email']

class BorrowedBookForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = ['reader', 'book', 'return_date']
