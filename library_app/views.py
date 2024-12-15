from django.shortcuts import render
from .models import Book, Reader, BorrowedBook
from django.views.generic import DetailView
from django.views.generic import CreateView
from .forms import BookForm, ReaderForm, BorrowedBookForm
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import MyAdministratorGroup
from django.contrib.auth.views import LoginView

def home(request):
    return render(request, 'library_app/home.html')


def book_list(request, available_only=False):
    if available_only:
        books = Book.objects.filter(is_available=True)
    else:
        books = Book.objects.all()

    context = {
        'books': books,
        'available_only': available_only,
    }
    return render(request, 'library_app/book_list.html', context)

def reader_list(request):
    readers = Reader.objects.all()
    context = {
        'readers': readers,
    }
    return render(request, 'library_app/reader_list.html', context)

def borrowed_book_list(request):
    borrowed_books = BorrowedBook.objects.select_related('reader', 'book').all()
    context = {
        'borrowed_books': borrowed_books,
    }
    return render(request, 'library_app/borrowed_book_list.html', context)


class ReaderDetailView(DetailView):
    model = Reader
    template_name = 'library_app/reader_detail.html'

# Представление для добавления книги
class BookCreateView(CreateView):
    form_class = BookForm
    template_name = 'library_app/add_book.html'
    success_url = '/books/'

# Представление для добавления читателя
class ReaderCreateView(CreateView):
    form_class = ReaderForm
    template_name = 'library_app/add_reader.html'
    success_url = '/readers/'

# Представление для добавления взятой книги
class BorrowedBookCreateView(CreateView):
    form_class = BorrowedBookForm
    template_name = 'library_app/add_borrowed_book.html'
    success_url = '/borrowed-books/'




# Представление для редактирования книги
class BookUpdateView(UpdateView):
    form_class = BookForm
    template_name = 'library_app/edit_book.html'
    queryset = Book.objects.all()
    success_url = '/books/'

# Представление для редактирования читателя
class ReaderUpdateView(UpdateView):
    form_class = ReaderForm
    template_name = 'library_app/edit_reader.html'
    queryset = Reader.objects.all()
    success_url = '/readers/'

# Представление для редактирования взятой книги
class BorrowedBookUpdateView(UpdateView):
    form_class = BorrowedBookForm
    template_name = 'library_app/edit_borrowed_book.html'
    queryset = BorrowedBook.objects.all()
    success_url = '/borrowed-books/'





class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library_app/delete_book_confirm.html'
    success_url = '/books/'

# Представление для удаления читателя
class ReaderDeleteView(DeleteView):
    model = Reader
    template_name = 'library_app/delete_reader_confirm.html'
    success_url = '/readers/'

# Представление для удаления взятой книги
class BorrowedBookDeleteView(DeleteView):
    model = BorrowedBook
    template_name = 'library_app/delete_borrowed_book_confirm.html'
    success_url = '/borrowed-books/'


class RegisterAdminView(LoginView):
    template_name = 'registration_admin.html'

    def get_context_data(request):
        form = AuthenticationForm(request)
        context = {
            'form': form,
        }
        return context

    def post(self, request):
        if request.method == 'POST':
            form = AuthenticationForm(request)
            if form.is_valid():
                user = form.save()
                user.groups.add(AdministratorGroup)
                return redirect('/admin/')
        else:
            return self.get_context_data(request)

    def get_success_url(self):
        return reverse('admin')