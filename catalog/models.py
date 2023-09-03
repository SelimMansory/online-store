from django.db import models

from users.models import User

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    """
    Модель категории
    """
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """
    Модель продуктов
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)

    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(verbose_name='превью', **NULLABLE)
    price = models.PositiveIntegerField(verbose_name='цена')
    create_date = models.DateField(verbose_name='дата создания', auto_now=True)
    date_of_change = models.DateField(verbose_name='дата изменения', auto_now_add=True)

    def __str__(self):
        return (f'{self.name} {self.description} {self.preview} \
{self.category} {self.price} {self.create_date} {self.date_of_change}')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')

    number_version = models.PositiveIntegerField(verbose_name='номер версии')
    title_version = models.CharField(max_length=150, verbose_name='название версии')
    current_version = models.BooleanField(verbose_name='признак текущий версии')

    def __str__(self):
        return f'{self.number_version} {self.title_version} {self.current_version}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'


class Contact(models.Model):
    """
    Модель контактов
    """
    country = models.CharField(max_length=50, verbose_name='страна')
    address = models.TextField(verbose_name='адрес')

    def __str__(self):
        return f'{self.country} {self.address}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'