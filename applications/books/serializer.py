from rest_framework import serializers
from applications.likes import services as likes_services
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
        fields = (
            'id', 'title',
            'author', 'description',
            'price', 'owner', 'category',
            'total_likes'
        )

    def get_is_fan(self, obj) -> bool:
        """
        Проверяет, лайкнул ли `request.user`, book (`obj`)
        """
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)





