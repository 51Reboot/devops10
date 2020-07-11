from django.contrib import admin
from .models import Publisher, Book

# Register your models here.

"""
    把app 出版社 定义在 admin 中
"""


class PublisherAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "address",
        "create_time",
        "update_time",
    ]


class BookAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "publisher_id",
        "create_time",
        "update_time",
    ]


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)

admin.site.site_header = "小年糕管理后台"
admin.site.site_title = "2020-小年糕"

