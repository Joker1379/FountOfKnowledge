# Generated by Django 2.2.2 on 2019-06-13 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190612_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='access',
            field=models.CharField(choices=[('standart', 'Пользователь'), ('moderator', 'Модератор'), ('admin', 'Администратор')], default='standart', max_length=20),
        ),
    ]
