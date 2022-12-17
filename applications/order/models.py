from django.contrib.auth import get_user_model
from django.db import models

from applications.books.models import Books

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='orders')
    count = models.PositiveIntegerField(default=1)
    order_confirm = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=88)
    confirm_code = models.CharField(max_length=88, default='', null=True, blank=True)

    def create_confirm_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.confirm_code = code