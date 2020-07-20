from django.db import models
from user.models import UserProfile

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=32,verbose_name='姓名')
    address = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return "{}:{}".format(self.name,self.address)

    class Meta:
        db_table = 'publisher'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name


# foreign key 要放在多的一方
class Book(models.Model):
    PUBLISHER_CHOISE = (
        (1,'发行中'),
        (2,'已发行'),
    )
    name = models.CharField(max_length=32)
    authors = models.ManyToManyField(to=UserProfile, null=True,blank=True,verbose_name='作者')
    desc = models.TextField(verbose_name='评论',null=True,default='好评',blank=True)
    publish_status = models.IntegerField(choices=PUBLISHER_CHOISE,default=2, verbose_name='发行状态')
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE, verbose_name='出版社')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name
