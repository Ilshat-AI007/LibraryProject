# from django.contrib import admin
# from .models import Book, Reader, BorrowedBook
# from django.contrib.admin.sites import AdminSite
# import models
# from .models import AdministratorGroup
#
# class AdministratorGroup(Group):
#     pass
# site.register(AdministratorGroup, AdminSite)
#
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = (
#         'title',
#         'author',
#         'publication_year',
#         'genre',
#         'publisher',
#         'is_available'
#     )
#
# @admin.register(Reader)
# class ReaderAdmin(admin.ModelAdmin):
#     list_display = (
#         'first_name',
#         'last_name',
#         'phone_number',
#         'email',
#         'registration_date'
#     )
#
# @admin.register(BorrowedBook)
# class BorrowedBookAdmin(admin.ModelAdmin):
#     list_display = (
#         'reader',
#         'book',
#         'borrow_date',
#         'return_date'
#     )
#


from django.contrib import admin
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group, User
from .models import Book, Reader, BorrowedBook
from .models import MyAdministratorGroup
from django.contrib import admin


# Регистрация модели группы администраторов
class AdministratorGroup(Group):
    pass


# Регистрация моделей в админке
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'publication_year',
        'genre',
        'publisher',
        'is_available'
    )


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'registration_date'
    )


@admin.register(BorrowedBook)
class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = (
        'reader',
        'book',
        'borrow_date',
        'return_date'
    )


# Представление для регистрации администратора
class RegisterAdminView(LoginRequiredMixin, View):
    template_name = 'registration_admin.html'

    def get(self, request):
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Администратор')
            user.groups.add(group)
            return redirect(reverse('admin:index'))
        else:
            context = {'form': form}
            return render(request, self.template_name, context)