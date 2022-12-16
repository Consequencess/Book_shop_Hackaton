from rest_framework import serializers

from applications.books.models import Category, Books


class CategorySerializer(serializers.ModelSerializer):
    """
    Серилизатор категорий
    """
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """
    Серилизатор книги
    """
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Books
        fields = '__all__'





