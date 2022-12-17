from django.contrib.contenttypes.models import ContentType
from django.db.models import Avg
from rest_framework import serializers

from applications.comments.serializer import CommentSerializer
from applications.likes import services as likes_services
from applications.books.models import Category, Books
from applications.ratings import services as ratings_services
from applications.ratings.models import Rating


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
    comments = CommentSerializer(many=True, read_only=True)
    is_fan = serializers.SerializerMethodField()
    is_reviewer = serializers.SerializerMethodField()
    total_rating = serializers.SerializerMethodField()

    class Meta:
        model = Books
        fields = (
            'id', 'title',
            'author', 'description',
            'price', 'owner', 'category',
            'is_fan',
            'total_likes',
            'total_rating',
            'is_reviewer',
            'comments'
        )

    def get_is_fan(self, obj) -> bool:
        """
        Проверяет, лайкнул ли `request.user`, book (`obj`)
        """
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)

    def get_is_reviewer(self, obj) -> bool:
        user = self.context.get('request').user
        return ratings_services.is_reviewer(obj, user)

    @staticmethod
    def get_total_rating(obj):
        obj_type = ContentType.objects.get_for_model(obj)
        ratings = Rating.objects.filter(
            content_type=obj_type, object_id=obj.id).aggregate(Avg('star'))['star__avg']
        return ratings






