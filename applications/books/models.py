from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


User = get_user_model()


class Category(models.Model):
    name = models.SlugField(primary_key=True)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Books'
        verbose_name = 'Book'

