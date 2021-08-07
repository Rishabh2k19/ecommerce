from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(_('Phone number'), unique=True,max_length=10)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []