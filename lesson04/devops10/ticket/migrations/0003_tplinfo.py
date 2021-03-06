# Generated by Django 2.2 on 2020-09-20 01:55

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='TplInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='变更时间')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='模板名称')),
                ('form_structure', jsonfield.fields.JSONField(default=dict, verbose_name='表单结构')),
                ('create_user', models.CharField(max_length=128, unique=True, verbose_name='创建者')),
                ('remarks', models.CharField(max_length=250, unique=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '模板',
                'verbose_name_plural': '模板',
                'db_table': 'p_tpl_info',
            },
        ),
    ]
