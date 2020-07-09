from django.contrib import admin
from .models import Publisher, Book
# Register your models here.

class PublisherAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'address',
        'create_time',
        'update_time'
    ]

class BookAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'publisher',
        'create_time',
        'update_time'
    ]

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)

admin.site.site_header = '51Reboot自动化'
admin.site.site_title = '第十期'
