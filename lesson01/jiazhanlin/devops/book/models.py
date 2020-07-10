from django.db import models
from user.models import UserProfile

# Create your models here.
'''
出版社
'''
class Publisher(models.Model):
    name = models.CharField('出版商', max_length=32)                  # 字段在admin后台显示为中文
    address = models.CharField(max_length=100, verbose_name='地址')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publisher'     # 默认自动生成的表名为：book_Publisher
        verbose_name = verbose_name_plural = '出版社'

'''
图书
'''
class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name='书名')
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE, verbose_name='出版社')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
        verbose_name = verbose_name_plural = '图书'


'''
作者
'''
class Author(models.Model):
    author = models.ManyToManyField(UserProfile, null=True, blank=True, verbose_name='作者')
    book = models.ManyToManyField(to='Book', verbose_name='书名')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = verbose_name_plural = '作者'
