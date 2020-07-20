from django.apps import AppConfig


class BookConfig(AppConfig):
    name = 'book'
    verbose_name = '图书管理系统'

    def ready(self):
        print("-------------------")
        from django.db.models.signals import pre_save, post_save
        from .signal import publisher_notice_to_dept
        from .models import Publisher

        post_save.connect(
            publisher_notice_to_dept,
            sender=Publisher,
            dispatch_uid="my_unique_identifier"
        )
