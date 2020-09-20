import os
import casbin
from django.conf import settings

from permission.models import CasbinRule
from permission.adapter import DjangoAdapter


def IsPermissionVerify(username, path, method):
    adapter_rule = DjangoAdapter(CasbinRule)
    model_conf_file = os.path.join(settings.BASE_DIR, "conf", "keymatch_model.conf")
    print("model_conf_file", model_conf_file)
    print(username, path, method)
    e = casbin.Enforcer(model_conf_file, adapter=adapter_rule)
    # e.add_function("keyMatchMethod", key_match_method_func)
    return e.enforce(username, path, method)