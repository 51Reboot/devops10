from django.contrib import admin
from .models import Publisher
from .models import  Book
# Register your models here.

class PublisherAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'address',
        'create_time',
        'update_time',
    ]


class BookAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'publisher',
        'create_time',
        'update_time',
    ]

admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Book,BookAdmin)

admin.site.site_header = '51reboot自动化'
admin.site.site_title = '第10期'
