# Generated by Django 2.2 on 2020-08-02 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0029_auto_20200802_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='名称'),
        ),
    ]
