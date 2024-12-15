# Generated by Django 5.1.4 on 2024-12-12 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('author', models.CharField(max_length=150, verbose_name='Автор')),
                ('publication_year', models.PositiveIntegerField(verbose_name='Год издания')),
                ('genre', models.CharField(max_length=100, verbose_name='Жанр')),
                ('publisher', models.CharField(max_length=150, verbose_name='Издательство')),
                ('is_available', models.BooleanField(default=True, verbose_name='Доступность')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('registration_date', models.DateField(auto_now_add=True, verbose_name='Дата регистрации')),
            ],
            options={
                'verbose_name': 'Читатель',
                'verbose_name_plural': 'Читатели',
            },
        ),
        migrations.CreateModel(
            name='BorrowedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField(auto_now_add=True, verbose_name='Дата взятия')),
                ('return_date', models.DateField(blank=True, null=True, verbose_name='Дата возврата')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readers_borrowed', to='library_app.book', verbose_name='Книга')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_borrowed', to='library_app.reader', verbose_name='Читатель')),
            ],
            options={
                'verbose_name': 'Взятая книга',
                'verbose_name_plural': 'Взятые книги',
            },
        ),
    ]
