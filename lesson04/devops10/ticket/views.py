import os
import shortuuid

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from .models import Classify
from .models import TplInfo
from .serializers import ClassifyModelSerializer
from .serializers import TplInfo
from .serializers import TplInfoModelSerializer
from .common import write_file


def JSONApiResponse(code, data, message):
    return Response({
        "code": code,
        "data": data,
        "message": message
    }, status=HTTP_200_OK)


def CommonPageNumberPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = "page_size"


class ClassifyModelViewSet(ModelViewSet):
    queryset = Classify.objects.all()
    serializer_class = ClassifyModelSerializer


class TplInfoModelViewSet(ModelViewSet):
    queryset = TplInfo.objects.all()
    serializer_class = TplInfoModelSerializer


class TaskAPIView(APIView):
    AbsPath = "/tmp/51Reboot/"
    fileExtensionDict = {"python": "py", "shell": "sh"}

    def get(self, request, *args, **kwargs):
        # ['ceshi02_5y2MneLgTz3zbeGAy9qsiR.py', 'ceshi02_3gWNrw49KokQ3xkdVoZh9o.py']
        # print(os.listdir(self.AbsPath))
        retdata = []
        for filename in os.listdir(self.AbsPath):
            name, uuid, create_user_classify = filename.split("_")
            create_user, classify = create_user_classify.split(".")
            retdata.append({
                "name": name,
                "classify": classify,
                "uuid": uuid,
                "filename": filename,
                "create_user": create_user,
            })
            print(name, uuid, create_user, classify)
        return JSONApiResponse(code=0, data=retdata, message=None)

    def post(self, request, *args, **kwargs):
        # {"name":"ceshi02","classify":"python","content":"#!/usr/bin/env python\n\nprint(\"hello world.\")"}
        # 获取所有Body参数
        data = request.data
        print(data)

        # 格式化路径和名称
        classify = self.fileExtensionDict.get(data['classify'], None)
        if not classify:
            return JSONApiResponse(code=-1, data=None, message="classify not support.")

        filename = self.gen_filepath(data['name'], classify)
        print("filename: {}".format(filename))
        result, ok = write_file(filename, data['content'])
        if not ok:
            return JSONApiResponse(code=-1, data=None, message=result)
        return JSONApiResponse(code=0, data=result, message=None)

    def gen_filepath(self, filename, classify, username='admin'):
        _uuid = shortuuid.uuid()
        filename = "{}{}_{}_{}.{}".format(self.AbsPath, filename, _uuid, username, classify)
        return filename



