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
    m2m_query()

def m2m_query():
    from book.models import Publisher, Book
    from user.models import UserProfile

    b = Book.objects.get(name='从卓越到优秀')
    authors = b.authors.all() # QuerySet
    for a in authors:
        print(a.username, a.phone, a.staff_id, a.email)

    u = UserProfile.objects.get(username='pc3')
    books = u.book_set.all()
    print(books)
    print('pc3发行', [ b.name for b in books])


def base_object_query():
    from book.models import Publisher, Book

    # Foreignkey 基于对象的查询
    b = Book.objects.get(name='从卓越到优秀')
    # 正向查询
    print("----正向查询----")
    print(b.name, b.desc, b.publisher_state, b.get_publisher_state_display())
    print(b.publisher_id)
    print(b.publisher.name, b.publisher.address)

    # 反向查询
    print("----反向查询----")
    p = Publisher.objects.get(name='人民出版社')
    print(p.book_set.all())  # QuerySet
    print([p.name for p in p.book_set.all()])
    book_info = []
    for b in p.book_set.all():
        book_info.append({
            'name': b.name,
            'desc': b.desc,
            'publisher_state': b.get_publisher_state_display(),
        })
        # print(b.name, b.desc, b.get_publisher_state_display())
    print(book_info)

def base_field_query():
    # Foreignkey 基于字段的查询
    from book.models import Publisher, Book

    # bs = Book.objects.filter(publisher__name='人民出版社')
    # print(bs)

    ps = Publisher.objects.filter(book__desc='非常好的书籍')
    print(ps)

    # # 正向查询
    # print("----正向查询----")
    # b = Book.objects.filter(publisher__name='人民出版社')
    # print(b.query)
    # for x in b.all():
    #     print(x.name, x.publisher.name, x.get_publisher_state_display())
    #
    # # 反向向查询
    # print("----反向查询----")
    # p = Publisher.objects.filter(book__name='Go源码分析')
    # print(p.query)
    # for x in p.all():
    #     print(x.name, x.address, x.book_set.all())


# 入口函数
def main():
    setup()

    logic()


if __name__ == '__main__':
    main()