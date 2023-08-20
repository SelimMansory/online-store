from django.db import models

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    """
    Модель продуктов
    """
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(verbose_name='превью', **NULLABLE)
    category = models.CharField(max_length=50, verbose_name='категория')
    price = models.PositiveIntegerField(verbose_name='цена')
    create_date = models.DateField(verbose_name='дата создания', auto_now=True)
    date_of_change = models.DateField(verbose_name='дата изменения', auto_now_add=True)

    def __str__(self):
        return (f'{self.name} {self.description} {self.preview} \
{self.category} {self.price} {self.create_date} {self.date_of_change}')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


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