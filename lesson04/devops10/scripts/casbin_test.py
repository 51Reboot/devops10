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
    import casbin

    from permission.models import CasbinRule
    from permission.adapter import DjangoAdapter

    adapter = DjangoAdapter(CasbinRule)

    e = casbin.Enforcer("./keymatch_model.conf", adapter)

    sub = "51reboot"  # the user that wants to access a resource.
    obj = "/api/v10/publisher/"  # the resource that is going to be accessed.
    act = "PUT"  # the operation that the user performs on the resource.

    if e.enforce(sub, obj, act):
        # permit alice to read data1
        print("允许")
    else:
        # deny the request, show an error
        print("拒绝")


    """
            for cr in self.adapter_model.objects.all():
            values = [x for x in cr.serializer().values() if x]
            # 'p, xiaoming, /api/v1/user/info, GET'
            persist.load_policy_line(', '.join(values), model)
    for cr in CasbinRule.objects.all():
    
        # print(cr.serializer().values())
        values = [x for x in cr.serializer().values() if x]
        print(', '.join(values))
    """




# 入口函数
def main():
    setup()

    logic()


if __name__ == '__main__':
    main()