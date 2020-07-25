class s():

    def fun2():
        return "fun2"


    def fun1():
        return 'fun1'


    def fun3():
        return 'fun3'
call_str = input("input which function you want to call :")

## 使用反射

if hasattr(s, call_str):
    obj = getattr(s, call_str)
    print(obj())
else:
    print("404 not Found")

