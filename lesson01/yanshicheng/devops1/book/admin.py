from django.contrib import admin

from .models import Authors, AuthorDetail, Publisher, Books

# Register your models here.




# 定义 admin 显示的作者类
class AuthorsAdmin(admin.ModelAdmin):
# 页面上显示的数据 字段
    list_display = [
        'name',
        'age',
        'authorDeail',
        'create_time',
        'update_time',
    ]

class AuthorDetailAdmin(admin.ModelAdmin):
    list_display = [
        'birthday',
        'telephone',
        'addr',
        'create_time',
        'update_time',
    ]

class PublisherAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'addr',
        'email',
        'create_time',
        'update_time',
    ]

class BooksAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'price',
        'good',
        'comment',
        # 'author',
        'publishs',
        'create_time',
        'update_time',
    ]

admin.site.register(Authors, AuthorsAdmin)
admin.site.register(AuthorDetail,AuthorDetailAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Books,BooksAdmin)

admin.site.site_header = 'OXO自动化系统'
admin.site.site_title = '这个Titl很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长!!'