# Generated by Django 4.2.4 on 2023-08-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mail_key',
            field=models.CharField(default='Aj8JQ0UawRztq5yPv4bTYW3GnEoXKO', max_length=30, verbose_name='ключ'),
        ),
    ]