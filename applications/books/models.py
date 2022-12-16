from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import Avg

from applications.likes.models import Like
from applications.ratings.models import Rating

User = get_user_model()


class Category(models.Model):
    """
    Моделька категорий
    """
    name = models.SlugField(primary_key=True)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    def __str__(self):
        return self.name


class Books(models.Model):
    """
    Моделька книги
    """
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=40)
    description = models.TextField()
    price = models.PositiveIntegerField(default=250)
    likes = GenericRelation(Like)
    ratings = GenericRelation(Rating)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def total_ratings(self):
        return Rating.objects.aggregate(Avg('star'))







