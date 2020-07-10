from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(AbstractUser):
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    staff_id = models.IntegerField(null=True, blank=True, verbose_name='工号')
    job_status = models.BooleanField(default=True, verbose_name='是否在职')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user_profile'
        verbose_name_plural = verbose_name = "员工"

'''
# settings.py
# 注册AUTH_USER_MODEL，使用应用User中的模型替换掉Django内置的User
AUTH_USER_MODEL = 'user.UserProfile'

# drop database devops;
# create database devops default charset=utf8;
python manage.py createsuperuser
python manage.py makemigrations && python manage.py migrate
'''