import casbin
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import CasbinRule
# 把数据库里面的数据加载到内存里面
from .adapter import DjangoAdapter
from .policy import key_match_method_func


def JSONApiResponse(code, data=None, message=None):
    return Response(
        {
            "code": code,
            "data": data,
            "message": message,
        },
        status=status.HTTP_200_OK
    )


class CheckRestApiPermission(APIView):

    authentication_classes = [JSONWebTokenAuthentication] # 传递token
    def get(self, request, *args, **kwargs):

        """

        casbin
            - http://casbin.51reboot.com/api/v1/auth

        http://casbin.51reboot.com/api/v1/auth?token=xxx&path=xxx&method=xxx


        """
        data = request.query_params
        path, method = data.get('path', None), data.get('method', None)
        if not path or not method:
            return JSONApiResponse(code=400, message='path and method is required.')

        adapter_rule = DjangoAdapter(CasbinRule)
        e = casbin.Enforcer(
            'permission/rbac_model2.conf',
            adapter=adapter_rule,
            enable_log=False,
        )
        e.add_function("keyMatchMethod", key_match_method_func)
        print("casbin: ", request.user.username, path, method)
        if e.enforce(request.user.username, path, method):
            return JSONApiResponse(code=0, message='Permission auth ok..')
        else:
            return JSONApiResponse(code=-1, message='Permission auth fail.')