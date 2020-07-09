from django.apps import AppConfig


class BookConfig(AppConfig):
    name = 'book'
    # 将应用名改为中文
    verbose_name = "图书管理系统"
