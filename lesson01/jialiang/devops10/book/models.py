from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=32,verbose_name='出版社名称')
    address = models.CharField(max_length=32,verbose_name='出版社地址')
    create_time = models.DateField(auto_now_add=True,verbose_name='创建时间',)
    update_time = models.DateField(auto_now=True, verbose_name='创建时间', )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publisher'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name


class Book(models.Model):
    name = models.CharField(max_length=32,verbose_name='书名')
    publisher = models.ForeignKey(to=Publisher,on_delete=models.CASCADE,verbose_name='出版社')
    create_time = models.DateField(auto_now_add=True,verbose_name='创建时间',)
    update_time = models.DateField(auto_now=True, verbose_name='创建时间', )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book'
        verbose_name = verbose_name_plural = '图书'

