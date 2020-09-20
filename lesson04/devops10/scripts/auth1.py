import os
import sys


# 初始化
def setup():
    BASEDIR = os.path.dirname(os.path.abspath(__file__))
    # print(BASEDIR)
    # print(os.path.abspath(os.path.join(BASEDIR, '..')))
    sys.path.insert(0, BASEDIR)
    sys.path.insert(0, os.path.abspath(os.path.join(BASEDIR, '..')))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops10.settings")

    import django
    django.setup()


# 业务逻辑
def logic():
    from rest_framework.authentication import TokenAuthentication
    from rest_framework.permissions import
    from django.contrib.auth.backends import RemoteUserBackend



# 入口函数
def main():
    setup()

    logic()


if __name__ == '__main__':
    main()