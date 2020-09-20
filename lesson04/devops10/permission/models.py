from django.db import models

# Create your models here.

# class CasbinRule(models.Model):
#
#     ptype = models.CharField(max_length=32)
#     v0 = models.CharField(max_length=32)
#     v1 = models.CharField(max_length=32)
#     v2 = models.CharField(max_length=32, null=True, blank=True)
#     v3 = models.CharField(max_length=32, null=True, blank=True)
#     v4 = models.CharField(max_length=32, null=True, blank=True)
#     v5 = models.CharField(max_length=32, null=True, blank=True)
#
#     class Meta:
#         db_table = 'casbin'
#         verbose_name_plural = verbose_name = '权限系统'
#
#     def serializer(self):
#         return {
#             'ptype' : self.ptype,
#             'v0': self.v0,
#             'v1': self.v1,
#             'v2': self.v2,
#             'v3': self.v3,
#             'v4': self.v4,
#             'v5': self.v5,
#         }


class CasbinRule(models.Model):
    CHOICE_PTYPE = (
        ('p', 'p'),
        ('g', 'g'),
    )

    ptype = models.CharField(max_length=1, choices=CHOICE_PTYPE, verbose_name="p | g")
    v0 = models.CharField(max_length=32, verbose_name="用户组 | 用户")
    v1 = models.CharField(max_length=32, verbose_name="PATH | 用户组")
    v2 = models.CharField(max_length=32, null=True, blank=True, verbose_name="METHOD")
    v3 = models.CharField(max_length=32, null=True, blank=True)
    v4 = models.CharField(max_length=32, null=True, blank=True)
    v5 = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.ptype, self.v0)

    class Meta:
        db_table = 'casbin_rule'
        verbose_name_plural = verbose_name = 'RESTful权限系统'

    def serializer(self):
        return {
            'ptype': self.ptype,
            'v0': self.v0,
            'v1': self.v1,
            'v2': self.v2,
            'v3': self.v3,
            'v4': self.v4,
            'v5': self.v5,
        }