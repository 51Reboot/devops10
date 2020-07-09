from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    phone = models.CharField('手机号',max_length=11)
    staff_id = models.IntegerField('员工编号', null=True, blank=True)
    job_status = models.BooleanField(default=True, verbose_name='员工在职状态')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user_profile'
        verbose_name_plural = verbose_name = '员工'