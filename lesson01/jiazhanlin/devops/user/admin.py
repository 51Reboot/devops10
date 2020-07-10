from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    list_display = (
        'username',
        'password',
        'staff_id',
        'job_status',
        'phone',
    )

    # 编辑布局
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        # 自定义字段展示
        (_('User Profile'), {'fields': ('phone', 'staff_id', 'job_status')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )