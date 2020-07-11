from django.contrib import admin
from .models import Publisher, Book


# Register your models here.
class PublisherAdmin(admin.ModelAdmin):
    # 在admin后台显示的字段
    list_display = [
        'name',
        'addr'
    ]


# 注册Publisher在admin后台显示
admin.site.register(Publisher, PublisherAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'publisher',
        'create_date',
        'update_date'
    ]


# 注册Book在admin后台显示
admin.site.register(Book, BookAdmin)

#  登陆修改 即admin登陆页面的名字
admin.site.site_header = '自动化后台管理系统'

# web页面title修改
admin.site.site_title = '自动化后台V1'
