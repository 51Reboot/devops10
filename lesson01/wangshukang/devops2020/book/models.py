from django.db import models

# Create your models here.

'''
  出版社
'''

class Publisher(models.Model):
    name = models.CharField('出版社名', max_length=32)
    address = models.CharField('出版社位置', max_length=100)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='修改时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publisher'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

'''
  图书
'''

class Book(models.Model):
    name = models.CharField('图书名称', max_length=32)
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE, verbose_name='出版社')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='修改时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name
