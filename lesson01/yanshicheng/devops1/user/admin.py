from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import UserProfile


# Register your models here.

class UserProfileAdmin(UserAdmin):
    # 要显示的字段
    list_display = (
        'username',
        'password',
        'phone',
        'staff_id',
        'jbo_status',
    )

    # 重写
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('用户信息'), {'fields': ('phone', 'staff_id', 'jbo_status')}),
    )


admin.site.register(UserProfile, UserProfileAdmin)