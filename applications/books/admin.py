from django.contrib import admin

from applications.books.models import Category, Books
from applications.images.models import Image


class ImageAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 10


class BooksAdmin(admin.ModelAdmin):
    inlines = [
        ImageAdmin
    ]
    list_display = ['id', 'title', 'books_count_like']

    def books_count_like(self, obj):
        return obj.likes.count()


admin.site.register(Category)
admin.site.register(Books, BooksAdmin)

