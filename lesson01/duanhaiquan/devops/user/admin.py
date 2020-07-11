from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import UserProfile
# Register your models here.


# class UserProfileAdmin(admin.ModelAdmin):
class UserProfileAdmin(UserAdmin):
    # 显示部分
    list_display = [
        "username",
        # "password",
        "email",
        "staff_id",
        "phone",
        "job_status",
        "is_active",
    ]

    # 编辑布局
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('员工信息10'), {'fields': ('phone', 'job_status', 'staff_id')}),
    )


admin.site.register(UserProfile, UserProfileAdmin)

# admin.site.site_header = "小年糕管理后台111"
# admin.site.site_title = "2020-小年糕111"
