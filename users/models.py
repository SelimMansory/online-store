from django.contrib.auth.models import AbstractUser
from django.db import models
from users.services import random_key

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=40, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    mail_key = models.CharField(max_length=30, default=random_key(),  verbose_name='ключ')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []