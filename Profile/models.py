import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
