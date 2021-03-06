# Generated by Django 2.2 on 2020-07-19 06:30

import book.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0025_auto_20200719_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=models.SET(book.models.get_default_publisher), to='book.Publisher', verbose_name='出版社'),
        ),
    ]
