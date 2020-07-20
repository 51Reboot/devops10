from django.contrib import admin
from .models import Publisher
from .models import Book


# 定义Admin
class PublisherAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'name',
        'address',
        'create_time',
        'update_time',
    ]

    search_fields = ('name', 'address')

    list_per_page = 15


class BookAdmin(admin.ModelAdmin):

    list_display = [
        'pk',
        'name',
        'publisher',
        'publisher_state',
        'desc_authors',
        'desc_short',
        'create_time',
        'update_time',
    ]

    filter_horizontal = ('authors', )

    def desc_authors(self, obj):
        return ','.join([ x.username for x in obj.authors.all() ])

    def desc_short(self, obj):
        MAX_LEGNTH = 15
        if len(obj.desc) > MAX_LEGNTH:
            return '{} ...'.format(obj.desc[:MAX_LEGNTH])
        return obj.desc

    desc_authors.short_description = '作者'
    desc_short.short_description = '评论'


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)

admin.site.site_header = '51Reboot自动化'
admin.site.site_title = '第十期'

