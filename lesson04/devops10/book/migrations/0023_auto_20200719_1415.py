# Generated by Django 2.2 on 2020-07-19 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0022_auto_20200719_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=14, on_delete=django.db.models.deletion.DO_NOTHING, to='book.Publisher', verbose_name='出版社'),
        ),
    ]
