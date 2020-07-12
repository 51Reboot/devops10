# Generated by Django 2.2 on 2020-07-11 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(verbose_name='生日')),
                ('telephone', models.CharField(max_length=32, verbose_name='手机号')),
                ('addr', models.CharField(max_length=64, verbose_name='住址')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '作者详情列表',
                'verbose_name_plural': '作者详情列表',
                'db_table': 'authordetail',
            },
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('authorDeail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book.AuthorDetail', verbose_name='详情')),
            ],
            options={
                'verbose_name': '作者列表',
                'verbose_name_plural': '作者列表',
                'db_table': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('addr', models.CharField(max_length=32, verbose_name='地址')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '出版社列表',
                'verbose_name_plural': '出版社列表',
                'db_table': 'Publisher',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, verbose_name='名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='价格')),
                ('good', models.IntegerField(default=1, verbose_name='好评')),
                ('comment', models.IntegerField(blank=True, null=True, verbose_name='评论')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('author', models.ManyToManyField(to='book.Authors', verbose_name='作者')),
                ('publishs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Publisher', verbose_name='出版社')),
            ],
            options={
                'verbose_name': '书籍列表',
                'verbose_name_plural': '书籍列表',
                'db_table': 'books',
            },
        ),
    ]
