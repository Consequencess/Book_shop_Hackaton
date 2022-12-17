from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Favorite(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey(User, verbose_name="User")

    def __str__(self):
        return self.user.email


