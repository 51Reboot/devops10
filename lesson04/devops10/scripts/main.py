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
    add_fk4()


def add_fk1():
    from book.models import Publisher, Book

    p = Publisher.objects.get(name='机械工业出版社')

    b = Book()
    b.name = 'Python 高并发实战'
    b.publisher_state = 2
    b.desc = 'Good'
    b.publisher = p  # ForeignKey
    b.save()


def add_fk2():
    from book.models import Publisher, Book

    b = Book.objects.get(name='从卓越到优秀')

    p = Publisher.objects.get(name='京师范大学出版社')
    p.book_set.add(b)


def add_fk3():
    from book.models import Publisher, Book

    b2 = Book.objects.get(name='海底两万里')
    b3 = Book.objects.get(name='幸福的时刻')

    p = Publisher.objects.get(name='京师范大学出版社')
    p.book_set.add(b2, b3)


def add_fk4():
    from book.models import Publisher, Book, UserProfile

    u1 = UserProfile.objects.get(username='zhengmoyu')
    u2 = UserProfile.objects.get(username='51reboot')
    u = UserProfile.objects.all()  # qs []

    b = Book.objects.get(name='Python 高并发实战')
    # b.authors.add(u1, u2)

    # b.authors.add(*u)
    # b.authors.remove(u1)
    # b.authors.remove(u1, u2)
    b.authors.clear()


# 入口函数
def main():
    setup()

    logic()


if __name__ == '__main__':
    main()