from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=32,verbose_name="名称")
    address = models.CharField(max_length=100,verbose_name="地址")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True,verbose_name="修改时间")

    def __str__(self):
        return self.name

    # 更改表名字
    class Meta:
        db_table = 'publisher'
        verbose_name = "出版社"
        verbose_name_plural = verbose_name


class Book(models.Model):
    name = models.CharField(max_length=32,verbose_name="名称")
    publisher = models.ForeignKey(to=Publisher,on_delete=models.CASCADE, verbose_name="出版社")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True,verbose_name="修改时间")

    def __str__(self):
        return self.name

    # 更改表名字
    class Meta:
        db_table = 'book'
        verbose_name = "图书"
        verbose_name_plural = verbose_name
