from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser

from rest_framework.renderers import JSONRenderer
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser


from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class ParseAPIView(APIView):

    parser_classes = [JSONParser, FormParser, MultiPartParser]
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request, *args, **kwargs):
        print(request.query_params)
        return Response(request.query_params)

    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response(request.data)


# 游客的身份
class Auth1APIView(APIView):

    # 认证
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return Response("Auth1")

    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response(request.data)

# 登录用户
class Auth2APIView(APIView):

    # 认证
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response("Auth2")

    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response(request.data)


from rest_framework.permissions import BasePermission


class IsCasbinVerify(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        import requests
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6IjUxcmVib290IiwiZXhwIjoxNTk2NjY4MzM0LCJlbWFpbCI6IjUxcmVib290QGdtYWkuY29tIn0.oEXdHaB4K7FivYPbQhZeY2AFcooPM0lD2a5iYnupNy4"
        url = "http://localhost:8000/api/v1/casbin/auth"
        # params = {
        #     "path": request.META['PATH_INFO'],
        #     "method": request.method,
        # }
        url = "{}?path={}&method={}".format(url, request.META['PATH_INFO'], request.method)
        headers = {
            "Authorization": "jwt {}".format(token)
        }
        print(url)
        req = requests.get(url, headers=headers)
        print(req.ok)
        print(req.url)
        print(req.json())
        if req.ok:
            jsondata = req.json()
            if jsondata['code'] == 0:
                return True
            else:
                errors = jsondata['message']
                print("errors: {}".format(errors))
                return False
        else:
            return False
        # return bool(request.user and request.user.is_staff)


# 后台管理员
class Auth3APIView(APIView):

    # 认证
    authentication_classes = [JSONWebTokenAuthentication] # sso | ldap
    # permission_classes = [IsAdminUser] # 权限系统
    permission_classes = [IsCasbinVerify] # 权限系统

    def get(self, request, *args, **kwargs):
        return Response("Auth3")

    def post(self, request, *args, **kwargs):
        return Response(request.data)