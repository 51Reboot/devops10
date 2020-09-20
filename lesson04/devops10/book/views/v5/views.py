from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.utils import jwt_decode_handler


from auth.verify import IsPermissionVerify


class TokenException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class IsTokenVerify(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        metadata = request.META
        path = metadata['PATH_INFO']
        method = request.method
        try:
            username = request.user.username
        except Exception as e:
            print("e", e)
            token = self.parse_token(request)
            username = self.get_username_by_token(token)

        print('request.user: ', username)
        print(username, path, method)
        # print(username, path, method, token)
        return IsPermissionVerify(username, path, method)
        # return True

    def parse_token(self, request):
        # Authorization: jwt xxx
        # Authorization: Token xxx
        http_authorization = request.META['HTTP_AUTHORIZATION']
        http_authorization_list = http_authorization.split()
        if len(http_authorization_list) != 2:
            raise TokenException("Token is required.")

        if http_authorization_list[0] != "jwt":
            raise TokenException("Token is isvalid.")

        return http_authorization_list[1]

    def get_username_by_token(self, token):
        try:
            decode_data = jwt_decode_handler(token)
            # {'username' : "xxx"}
        except Exception as e:
            print("e: ", e)
            return ""

        return decode_data['username']


class TestPermission(APIView):
    authentication_classes = [JSONWebTokenAuthentication]  # request.user
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsTokenVerify]

    def get(self, request, *args, **kwargs):
        return Response("GET")

    def post(self, request, *args, **kwargs):
        return Response("POST")