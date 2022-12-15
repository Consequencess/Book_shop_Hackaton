from django.contrib import admin

from applications.books.models import Books, Category
admin.site.register(Category)
admin.site.register(Books)

