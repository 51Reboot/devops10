from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.

# class UserProfile(models.Model):
# 自定义user表字段，需要在setting设置 AUTH_USER_MODEL = 'user.UserProfile'
class UserProfile(AbstractUser):
    phone = models.CharField(max_length=11, verbose_name='手机号码')
    staff_id = models.IntegerField(null=True, blank=True, verbose_name='员工编号')
    job_status = models.BooleanField(default=True, verbose_name='员工在职状态')

    def __str__(self):
        return '员工：{}'.format(self.username)

    class Meta:
        db_table = 'user_profile'
        ordering = ['id']
        verbose_name = verbose_name_plural = '员工'
