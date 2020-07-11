from django.db import models

# Create your models here.


class Publisher(models.Model):

    name = models.CharField(max_length=32, verbose_name="出版社名称")
    address = models.CharField(max_length=100, verbose_name="出版社地址")
    postcode = models.CharField(max_length=10, verbose_name="邮编")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "publisher"
        verbose_name = "出版社1"
        # 负数改成单数
        verbose_name_plural = verbose_name


class Book(models.Model):

    name = models.CharField(max_length=100, verbose_name="图书名")
    publisher_id = models.ForeignKey(to=Publisher, on_delete=models.CASCADE,verbose_name="出版社名称")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "book"
        verbose_name = "图书"
        # 负数改成单数
        verbose_name_plural = verbose_name
