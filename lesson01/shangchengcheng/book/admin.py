from django.contrib import admin
from .models import Publisher, Books, Author
# Register your models here.


class PublisherAdmin(admin.ModelAdmin):
    # 在后台中显示字段
    list_display = (
        'name',
        'address',
        'create_time',
        'update_time',
    )


# 将PublisherAdmin 注册到admin中
admin.site.register(Publisher, PublisherAdmin)
admin.site.site_header = "Books Manager System"
admin.site.site_title = "Books"


class BooksAdmin(admin.ModelAdmin):
    # 在后台中显示字段
    list_display = (
        'name',
        'publisher',
        'create_time',
        'update_time',
    )


# 将books 注册到admin中
admin.site.register(Books, BooksAdmin)


class AuthorAdmin(admin.ModelAdmin):
    # 在后台中显示字段
    list_display = (
        'name',
    )


# 将PublisherAdmin 注册到admin中
admin.site.register(Author, AuthorAdmin)
