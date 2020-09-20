import casbin


e = casbin.Enforcer("./keymatch_model.conf", "./keymatch_policy.csv")

def f1():
    # request.user
    sub = "alice"                # the user that wants to access a resource.

    # request.META['PATH_INFO']
    obj = "/api/v10/publisher/"  # the resource that is going to be accessed.

    # request.method
    act = "DELETE"                  # the operation that the user performs on the resource.


    if e.enforce(sub, obj, act):
        # permit alice to /api/v10/publisher/ GET
        print("允许")
    else:
        # deny the request, show an error
        print("拒绝")


def f2():
    # request.user
    sub = "admin"                # the user that wants to access a resource.

    # request.META['PATH_INFO']
    obj = "/api/x/x/x/xxxxfdasfafa"  # the resource that is going to be accessed.

    # request.method
    act = "PATCH"                  # the operation that the user performs on the resource.


    if e.enforce(sub, obj, act):
        # permit alice to /api/v10/publisher/ GET
        print("允许")
    else:
        # deny the request, show an error
        print("拒绝")


def f3():
    # request.user
    sub = "51reboot"                # the user that wants to access a resource.

    # request.META['PATH_INFO']
    obj = "/api/v1/51reboot/publisher"  # the resource that is going to be accessed.

    # request.method
    act = "GET"                  # the operation that the user performs on the resource.


    if e.enforce(sub, obj, act):
        # permit alice to /api/v10/publisher/ GET
        print("允许")
    else:
        # deny the request, show an error
        print("拒绝")


f3()

from casbin import persist

