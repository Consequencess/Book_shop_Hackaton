from django.contrib import admin

from applications.books.models import Category, Books


class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'books_count_like']

    def books_count_like(self, obj):
        return obj.likes.count()


admin.site.register(Category)
admin.site.register(Books, BooksAdmin)

