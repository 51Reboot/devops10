from django.db import models
from user.models import UserProfile

from .validate import validate_publisher_state
from django.core.validators import validate_ipv4_address
from django.core.exceptions import ValidationError

# Create your models here.





'''
    出版社
'''


class Publisher(models.Model):

    name = models.CharField(
        # unique=True,
        max_length=32,
        verbose_name='名称'
        )
    address = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='地址'
    )
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return '{}: {}'.format(self.name, self.address)

    class Meta:
        # 元数据 book_publisher
        db_table = 'publisher'
        verbose_name = verbose_name_plural = '出版社'


def get_default_publisher():
    return Publisher.objects.get(name='默认出版社')

'''
    图书
    ForeignKey 要放到多的一方
'''


class Book(models.Model):
    PUBLISHER_CHOICE = (
        (1, '发行中'),
        (2, '已发行'),
    )

    name = models.CharField(max_length=32, verbose_name='书名')
    # 一对多| 多对一
    publisher = models.ForeignKey(
        to=Publisher,
        on_delete=models.SET(get_default_publisher),
        verbose_name='出版社'
    )
    publisher_state = models.IntegerField(
        validators=[validate_publisher_state, ],
        choices=PUBLISHER_CHOICE,
        verbose_name='出版社状态'
    )
    authors = models.ManyToManyField(
        to=UserProfile,
        null=True,
        blank=True,
        verbose_name='作者'
    )
    desc = models.TextField(
        # validators=[validate_ipv4_address,],
        null=True,
        blank=True,
        verbose_name='评论'
    )
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return "<object {}>".format(self.name)

    class Meta:
        db_table = 'book'
        verbose_name = verbose_name_plural = '图书'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # create
        # update
        # print(self.publisher_state, self.PUBLISHER_CHOICE)
        if self.publisher_state not in [ x[0] for x in self.PUBLISHER_CHOICE ]:
            raise ValidationError("{} not {}".format(self.publisher_state, self.PUBLISHER_CHOICE))
        super(Book, self).save(force_insert=False, force_update=False, using=None,
             update_fields=None)


