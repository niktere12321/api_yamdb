from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    USER_ROLES = (
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
    )
    bio = models.TextField(max_length=500, blank=True)
    role = models.CharField(
        max_length=16,
        choices=USER_ROLES,
        default=USER
    )

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR
