from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import mixins

from rest_framework import viewsets

from book.models import Publisher
from book.models import Book
from book.views.v2.serialization import PublisherSerializer
from book.views.v2.serialization import BookModelSerializer




class PublishAPIView(APIView):

    def get(self, request, *args, **kwargs):
        # 序列化
        # for k, v in request.META.items():
        #     print(k, v)
        # print(request.META['CONTENT_TYPE'])
        # print(request.GET)  # Django
        # print(request.query_params) # DRF
        print(args)
        # http://localhost:8000/api/v2/publish_v2/14/
        print(kwargs)  # {'pk' : 14}
        pk = kwargs.get('pk', None)
        if pk:
            # instance = Publisher.objects.get(pk=pk)\
            try:
                instance = Publisher.objects.get(pk=pk)
            except Publisher.DoesNotExist as e:
                return Response("{}记录不存在".format(pk))

            s = PublisherSerializer(instance)
        else:
            instances = Publisher.objects.all()
            s = PublisherSerializer(instances, many=True)
        return Response(s.data)
        # return JsonResponse(s.data, safe=False)
        # return HttpResponse("APIView GET view v2")

    def post(self, request, *args, **kwargs):
        # 反序列化
        # print(request.body)
        # print(request.POST)  # Django
        # print(request.data)  # DRF
        data = request.data
        s = PublisherSerializer(data=data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(s.errors)
        # return HttpResponse("APIView POST view v2")

    def put(self, request, *args, **kwargs):
        data = request.data
        pk = kwargs.get('pk', None)
        if not pk:
            return Response("pk is required.")
        instance = Publisher.objects.get(pk=pk)
        s = PublisherSerializer(instance, data=data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(s.errors)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response("pk is required.")
        try:
            instance = Publisher.objects.get(pk=pk)
        except Publisher.DoesNotExist as e:
            return Response("{}记录不存在".format(pk))
        instance.delete()
        return Response("删除成功.")


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


from rest_framework_jwt.authentication import JSONWebTokenAuthentication
class PublishGenericAPIView(GenericAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    authentication_classes = [JSONWebTokenAuthentication]  # sso | ldap
    permission_classes = [IsCasbinVerify]  # 权限系统


    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk:
            instance = self.get_object()
            s = self.get_serializer(instance)
            # try:
            #     instance = Publisher.objects.get(pk=pk)
            # except Publisher.DoesNotExist as e:
            #     return Response("{}记录不存在".format(pk))
            #
            # s = PublisherSerializer(instance)
        else:
            s = self.get_serializer(self.get_queryset(), many=True)
            # instances = Publisher.objects.all()
            # s = PublisherSerializer(instances, many=True)
        return Response(s.data)

    def post(self, request, *args, **kwargs):
        s = self.get_serializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(s.errors)

        # data = request.data
        # s = PublisherSerializer(data=data)
        # if s.is_valid():
        #     s.save()
        #     return Response(s.data)
        # else:
        #     return Response(s.errors)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        s = self.get_serializer(instance=instance, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(s.errors)

        # data = request.data
        # pk = kwargs.get('pk', None)
        # if not pk:
        #     return Response("pk is required.")
        # instance = Publisher.objects.get(pk=pk)
        # s = PublisherSerializer(instance, data=data)
        # if s.is_valid():
        #     s.save()
        #     return Response(s.data)
        # else:
        #     return Response(s.errors)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response("删除成功.")
        # pk = kwargs.get('pk', None)
        # if not pk:
        #     return Response("pk is required.")
        # try:
        #     instance = Publisher.objects.get(pk=pk)
        # except Publisher.DoesNotExist as e:
        #     return Response("{}记录不存在".format(pk))
        # instance.delete()
        # return Response("删除成功.")


class BookGenericAPIView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk:
            instance = self.get_object()
            s = self.get_serializer(instance)
        else:
            s = self.get_serializer(self.get_queryset(), many=True)
        return Response(s.data)

    def post(self, request, *args, **kwargs):
        s = self.get_serializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(s.errors)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        s = self.get_serializer(instance=instance, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(s.errors)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response("删除成功.")


class PublishMixinGenericAPIView(mixins.ListModelMixin,
                                 mixins.CreateModelMixin,
                                 mixins.RetrieveModelMixin,
                                 mixins.UpdateModelMixin,
                                 mixins.DestroyModelMixin,
                                 GenericAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PublishV2MixinGenericAPIView(ListAPIView,
                                   CreateAPIView,
                                   UpdateAPIView,
                                   RetrieveAPIView,
                                   DestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter


class CustormPageNumberPagination(PageNumberPagination):
    # 设置每页的条数
    page_size = 2

    # 动态设置每页的条数
    page_size_query_param = 'page_size'

    # 最大每页显示多少条数据
    max_page_size = 100


class PublishViewSet(
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet
                ):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    pagination_class = CustormPageNumberPagination

    # 过滤器
    # ?search=南京
    # ?search=河北
    filter_backends = [SearchFilter]
    search_fields = ['name', 'address']


class PublishModelViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
