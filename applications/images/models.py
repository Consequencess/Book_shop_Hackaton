from django.db import models

from applications.books.models import Books


class Image(models.Model):
    post = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    fields = 'total_likes'
