from django.contrib import admin
from .models import *

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


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.site_header = '自动化运维平台'
admin.site.site_title = '自动化运维平台'