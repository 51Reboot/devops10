from django.contrib import admin
from .models import Publisher
from .models import Book

# Register your models here.


class PublishAdmin(admin.ModelAdmin):
     list_display = [
         'name',
         'address',
         'create_time',
         'update_time',
     ]

class BookAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'pulisher',
        'create_time',
        'update_time',
    ]


admin.site.register(Publisher, PublishAdmin)
admin.site.register(Book, BookAdmin)

admin.site.site_header = '图书管理系统'
admin.site.site_title = 'book'