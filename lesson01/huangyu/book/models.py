from django.db import models


# Create your models here.

# 表名：pulisher
class Publisher(models.Model):
    name = models.CharField(max_length=32, verbose_name='名称')
    address = models.CharField(max_length=100, verbose_name='地址')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return '{}: {}'.format(self.name, self.address)

    class Meta:
        db_table = 'pulisher'
        verbose_name = verbose_name_plural = '出版社'


class Book(models.Model):
    name = models.CharField(max_length=32, verbose_name='书名')
    pulisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE, verbose_name='出版社')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book'
        verbose_name = verbose_name_plural = '图书'
