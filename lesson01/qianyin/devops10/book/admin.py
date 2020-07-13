from django.contrib import admin

# Register your models here.

from .models import Publisher,Book


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
admin.site.site_header = '51reboot自动化班'
admin.site.site_title = '第十期'
