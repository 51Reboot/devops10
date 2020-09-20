from django.apps import AppConfig


class BookConfig(AppConfig):
    name = 'book'
    verbose_name = '图书管理系统'

    def ready(self):
        from django.db.models.signals import pre_save, post_save, post_delete, post_init
        from django.db.models.signals import m2m_changed
        from .signal import publisher_notice_to_dept
        from .signal import publisher_notice_to_dept_delete
        from .signal import m2m_signal_handler
        from .models import Publisher
        from .models import Book

        # post_init.connect(
        #     publisher_notice_to_dept,
        #     sender=Publisher,
        #     dispatch_uid="my_unique_identifier1"
        # )

        # post_save.connect(
        #     publisher_notice_to_dept,
        #     sender=Publisher,
        #     dispatch_uid="my_unique_identifier1"
        # )
        #
        # post_delete.connect(
        #     publisher_notice_to_dept_delete,
        #     sender=Publisher,
        #     dispatch_uid="my_unique_identifier2"
        # )

        # post_save.connect(
        #     m2m_signal_handler,
        #     sender=Book,
        #     dispatch_uid="m2m_post_save"
        # )

        m2m_changed.connect(
            m2m_signal_handler,
            sender=Book.authors.through,
            dispatch_uid="m2m_post_change"
        )