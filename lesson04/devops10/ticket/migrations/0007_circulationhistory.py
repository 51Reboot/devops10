# Generated by Django 2.2 on 2020-09-20 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_taskinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CirculationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='变更时间')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='工单标题')),
                ('state', models.CharField(max_length=100, verbose_name='工单状态')),
                ('source', models.CharField(max_length=100, verbose_name='源节点ID')),
                ('target', models.CharField(max_length=100, verbose_name='目标节点ID')),
                ('circulation', models.CharField(max_length=100, verbose_name='流转ID')),
                ('processor', models.CharField(max_length=100, verbose_name='处理人')),
                ('processor_id', models.CharField(max_length=100, verbose_name='处理人ID')),
                ('cost_duration', models.CharField(max_length=100, verbose_name='处理时长')),
                ('remarks', models.CharField(max_length=250, unique=True, verbose_name='备注')),
                ('work_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.WorkOrderInfo', verbose_name='工单ID')),
            ],
            options={
                'verbose_name': '工单流转历史',
                'verbose_name_plural': '工单流转历史',
                'db_table': 'p_work_order_circulation_history',
            },
        ),
    ]
