from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=32, verbose_name="出版社名称")
    address = models.CharField(max_length=100, verbose_name="出版社地址")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.name

    # 重新定义表名
    class Meta:
        db_table = 'publisher'
        # 将verbose_name变成单数形式，不然在后台中文后面会增加一个s
        verbose_name_plural = verbose_name = "出版社"


class Books(models.Model):
    name = models.CharField(max_length=32, verbose_name="图书名称")
    publisher = models.ForeignKey(
        to=Publisher, on_delete=models.CASCADE, verbose_name="出版社")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.name

    # 重新定义表名
    class Meta:
        db_table = 'books'
        # 将verbose_name变成单数形式，不然在后台中文后面会增加一个s
        verbose_name_plural = verbose_name = "图书"


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="作者")
    books = models.ManyToManyField(to=Books, verbose_name="图书")

    def __str__(self):
        return self.name

    # 重新定义表名
    class Meta:
        db_table = 'author'
        # 将verbose_name变成单数形式，不然在后台中文后面会增加一个s
        verbose_name_plural = verbose_name = "作者"
