import casbin


"""
path/to/model.conf    # 匹配的规则
path/to/policy.csv    # 数据库存储权限数据
"""
e = casbin.Enforcer("keymatch_model.conf", "keymatch_policy.csv")
print(e)


sub = "xiaoming"  # token
obj = "/api/v1/user/info"
act = "POST"

if e.enforce(sub, obj, act):
    # permit alice to read data1
    print("权限通过")
else:
    # deny the request, show an error
    print("权限拒绝")