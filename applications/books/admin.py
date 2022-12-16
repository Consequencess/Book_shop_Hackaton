from django.contrib import admin

from applications.books.models import Category, Books


class PostAdmin(admin.ModelAdmin):
    # inlines = [
        # ImageAdmin
    # ]
    list_display = ['id', 'title', 'books_count_like']

    def post_count_like(self, obj):
        return obj.likes.filter(like=True).count()


admin.site.register(Category)
admin.site.register(Books)
