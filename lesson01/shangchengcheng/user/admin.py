from django.contrib import admin
from .models import UserProfile
# 增加了密码字段验证以及隐藏密码不以明文方式来显示密码
from django.contrib.auth.admin import UserAdmin
# Register your models here.
# class UserAdmin(admin.ModelAdmin):


class UserProfileAdmin(UserAdmin):
    list_display = (
        'username',
        'password',
        'phone',
        'staff_id',
        'job_status',
    )
    # 将父类的这个元组重写，在admin后台添加用户时才会显示除用户和密码的其他字段
    fieldsets = (
        (None, {'fields': ('username', 'password', 'staff_id', 'phone')}),
    )


admin.site.register(UserProfile, UserProfileAdmin)
