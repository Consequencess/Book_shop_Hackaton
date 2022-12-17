from django.contrib.auth import get_user_model
from django.db import models

from applications.books.models import Books

User = get_user_model()


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comments', null=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='comments')
    commentary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner.email} {self.post.title}'