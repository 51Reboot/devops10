from django.contrib import admin
from .models import Publisher, Book
# Register your models here.


# 定义admin
class PublisherAdmin(admin.ModelAdmin):
    # admin页面显示的字段
    list_display = (
        'name',
        'address',
        'create_time',
        'update_time',
    )


class BookAdmin(admin.ModelAdmin):
    # admin页面显示的字段
    list_display = (
        'name',
        'publisher',
        'create_time',
        'update_time',
    )


# 注册admin
admin.site.register(Publisher, PublisherAdmin)

admin.site.register(Book, BookAdmin)

# 登录修改 即admin登录页面名字
admin.site.site_header = "51reboot自动化"

# web页面title修改
admin.site.site_title = "2020年"


