# Generated by Django 2.2.13 on 2020-07-17 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_book_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.TextField(blank=True, default='好评', null=True, verbose_name='评论'),
        ),
    ]
