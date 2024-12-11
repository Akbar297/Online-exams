from django.db import models

from django.contrib.auth.models import AbstractUser

ROLES = (
    (1, 'Teacher'),
    (2, 'Student'),
)


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)

    role = models.IntegerField(choices=ROLES, default=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


