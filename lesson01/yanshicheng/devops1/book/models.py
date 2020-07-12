# from django.db import models
#
# # Create your models here.
# class Publisher(models.Model):
#
#     name = models.CharField(max_length=32, verbose_name='名称')
#     address = models.CharField(max_length=100, verbose_name='地址')
#     create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#     update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
#
#     def __str__(self):
#         return '{}: {}'.format(self.name, self.address)
#
#     class Meta:
#         # 元数据 book_publisher
#         db_table = 'publisher'
#         verbose_name = verbose_name_plural = '出版社'
from django.db import models

# Create your models here.

# 作者表
class Authors(models.Model):
    name = models.CharField(max_length=32,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')# ,to_field='id'
    authorDeail = models.OneToOneField(to="AuthorDetail",on_delete=models.CASCADE,verbose_name='详情') # to_field='id'   自动指向主键on_delete=models.CASCADE 不做级联: on_delete=models.SET_NULL
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    def __str__(self):
        return self.name

    class Meta:
        # 元数据 book_publisher
        db_table = 'authors'
        verbose_name = verbose_name_plural = '作者列表'
# 作者详细表
class AuthorDetail(models.Model):
    birthday = models.DateField(verbose_name='生日')
    telephone = models.CharField(max_length=32,verbose_name='手机号')
    addr = models.CharField(max_length=64,verbose_name='住址')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    def __str__(self):
        return self.addr
    class Meta:
        # 元数据 book_publisher
        db_table = 'authordetail'
        verbose_name = verbose_name_plural = '作者详情列表'

# 出版社表
class Publisher(models.Model):
    name = models.CharField(max_length=32,verbose_name='名称')
    addr = models.CharField(max_length=32,verbose_name='地址')
    email = models.EmailField(verbose_name='邮箱')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    def __str__(self):
        return self.name
    class Meta:
        # 元数据 book_publisher
        db_table = 'Publisher'
        verbose_name = verbose_name_plural = '出版社列表'


# 书籍表
class Books(models.Model):
    title = models.CharField(max_length=16, verbose_name='名称')
    price = models.DecimalField(max_digits=5, decimal_places=2,verbose_name='价格')
    good = models.IntegerField(default=1, verbose_name='好评')
    comment = models.TextField(null=True, blank=True,verbose_name='评论')
    author = models.ManyToManyField(to='Authors', verbose_name='作者')
    publishs = models.ForeignKey(to='Publisher', on_delete=models.CASCADE,verbose_name='出版社') # ,to_field='id'
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    def __str__(self):
        return self.title
    class Meta:
        # 元数据 book_publisher
        db_table = 'books'
        verbose_name = verbose_name_plural = '书籍列表'

# 手动创建第三张表 用于特殊需求,自定义字段等,但是不能使用部分 django 提供的方法
#
# class BookToAuthor(models.Model):
#     book_id = models.ForeignKey(to='Book')
#     author = models.ForeignKey(to='Author')

