# Generated by Django 2.2 on 2020-09-20 02:31

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0008_auto_20200920_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='变更时间')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='任务名称')),
                ('structure', jsonfield.fields.JSONField(default=dict, verbose_name='流程结构')),
                ('tpls', jsonfield.fields.JSONField(default=dict, verbose_name='模版')),
                ('task', jsonfield.fields.JSONField(default=dict, verbose_name='模任务ID, array, 可执行多个任务，可以当成通知任务，每个节点都会去执行版')),
                ('submit_count', models.IntegerField(default=0, verbose_name='提交统计')),
                ('create_user', models.CharField(max_length=128, unique=True, verbose_name='创建者')),
                ('notice', jsonfield.fields.JSONField(default=dict, verbose_name='绑定通知')),
                ('classify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Classify', verbose_name='分类ID')),
            ],
            options={
                'verbose_name': '流程',
                'verbose_name_plural': '流程',
                'db_table': 'p_process_info',
            },
        ),
    ]
