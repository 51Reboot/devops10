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
    search_fields = ('name', 'address')


class BookAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'publisher',
        'publish_status',
        'desc_authors',
        'desc_short',
        'create_time',
        'update_time',
    ]

    filter_horizontal = ('authors',)

    def desc_authors(self,obj):
        return ','.join([x.username for x in obj.authors.all()])

    def desc_short(self, obj):
        MAX_LENGHT = 15
        if len(obj.desc) > MAX_LENGHT:
            return "{}...".format(obj.desc[:MAX_LENGHT])
        return obj.desc

    desc_authors.short_description = '作者'
    desc_short.short_description = '评论'

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.site_header = '51reboot自动化班'
admin.site.site_title = '第十期'
