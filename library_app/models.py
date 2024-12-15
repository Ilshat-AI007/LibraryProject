from django.db import models
from django.contrib.auth.models import Group


class MyAdministratorGroup(Group):
    class Meta:
        verbose_name = 'Группа администраторов'
        verbose_name_plural = 'Группы администраторов'

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    author = models.CharField(max_length=150, verbose_name="Автор")
    publication_year = models.PositiveIntegerField(verbose_name="Год издания")
    genre = models.CharField(max_length=100, verbose_name="Жанр")
    publisher = models.CharField(max_length=150, verbose_name="Издательство")
    is_available = models.BooleanField(default=True, verbose_name="Доступность")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title



class Reader(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Электронная почта")
    registration_date = models.DateField(auto_now_add=True, verbose_name="Дата регистрации")

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BorrowedBook(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name="books_borrowed", verbose_name="Читатель")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="readers_borrowed", verbose_name="Книга")
    borrow_date = models.DateField(auto_now_add=True, verbose_name="Дата взятия")
    return_date = models.DateField(blank=True, null=True, verbose_name="Дата возврата")

    class Meta:
        verbose_name = "Взятая книга"
        verbose_name_plural = "Взятые книги"

    def __str__(self):
        return f"{self.reader} взял книгу '{self.book}'"