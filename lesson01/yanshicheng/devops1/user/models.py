from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    phone = models.CharField(max_length=11, verbose_name='手机号')
    staff_id = models.IntegerField(null=True, blank=True,verbose_name='员工编号')
    jbo_status = models.BooleanField(default=True, verbose_name='员工在职状态')

    def __str__(self):
        return self.phone

    class Meta:
        db_table = 'user_profile'
        verbose_name_plural = verbose_name = '员工'
