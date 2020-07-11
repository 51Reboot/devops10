from django.db import models


# Create your models here.

class Publisher(models.Model):
    """
        出版社
    """
    name = models.CharField(max_length=32, verbose_name='出版社名称')
    addr = models.CharField(max_length=256, verbose_name='出版社地址')

    def __str__(self):
        return '出版社-{}'.format(self.name)

    class Meta:  # 元数据信息 book_publisher
        # 数据库表名
        db_table = 'Publisher'
        # verbose_name 别名
        verbose_name = verbose_name_plural = '出版社'
        # 按照id排列顺序
        ordering = ['id']


class Book(models.Model):
    """
        图书
        foreginkey放在多的一边
    """
    name = models.CharField(max_length=128, verbose_name='书名')
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE, verbose_name='出版社')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # auto_now_add 第一次插入数据的时间
    update_date = models.DateTimeField(auto_now=True, verbose_name='更新时间')  # auto_now 每次数据更新，都会更新这个时间

    def __str__(self):
        return '图书-{}'.format(self.name)

    class Meta:
        db_table = 'book'
        verbose_name = verbose_name_plural = '图书'
        ordering = ['id']
