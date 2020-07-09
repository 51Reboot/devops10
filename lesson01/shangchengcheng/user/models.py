from django.db import models
# 导入django中的user
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(AbstractUser):
    phone = models.CharField(max_length=11, verbose_name='手机号')
    staff_id = models.CharField(max_length=30, null=True, verbose_name='员工编号')
    job_status = models.BooleanField(default=True, verbose_name="员工在职状态")

    def __str__(self):
        return self.phone
    
    class Mate:
        db_table = 'user_profile'
        verbose_name_plural = verbose_name = "员工"