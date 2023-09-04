from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    """
    Модель блога
    """
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    context = models.TextField(verbose_name='описание')
    preview = models.ImageField(verbose_name='превью', **NULLABLE)
    create = models.DateField(verbose_name='дата создания', auto_now=True)
    is_publish = models.BooleanField(verbose_name='статус публикации', default=True)
    count_views = models.IntegerField(verbose_name='счётчик просмотров', default=0)

    def __str__(self):
        return (f"{self.title} {self.slug} {self.context} {self.preview} {self.create} \
{self.is_publish} {self.count_views}")

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'