# Generated by Django 2.2.13 on 2020-07-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publish_status',
            field=models.IntegerField(choices=[(1, '发行中'), (2, '已发行')], default=2, verbose_name='发行状态'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=32, verbose_name='姓名'),
        ),
    ]