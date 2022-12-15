from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from applications.books.models import Books

User = get_user_model()


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    post = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='ratings')
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ], blank=True, null=True
    )

    def __str__(self):
        return f'{self.owner} -> {self.rating}'