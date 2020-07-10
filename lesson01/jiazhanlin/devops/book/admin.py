from django.contrib import admin
from .models import Publisher, Book, Author

# Register your models here.

admin.site.site_header = '51Reboot自动化'
admin.site.site_title = '第十期'

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'create_time',
        'update_time',
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'publisher',
        'create_time',
        'update_time',
    )


# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = (
#         'book',
#         'Author',
#         'create_time',
#         'update_time',
#     )

