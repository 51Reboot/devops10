from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Publisher


@receiver(pre_save, sender=Publisher)
def publisher_notice_to_dept(sender, **kwargs):
    '''
    新增一个出版社之前我要发送一封通知邮件
    :param sender:
    :param kwargs:
    :return:
    '''
    print(sender)
    print(kwargs)