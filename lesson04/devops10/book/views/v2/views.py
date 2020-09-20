from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse

from book.models import Publisher
from book.models import Book
from book.views.v2.serialization import PublisherSerializer
from book.views.v2.serialization import BookModelSerializer


class PublishViewV1(APIView):

    def get(self, request, *args, **kwargs):
        print(request.GET)  # Django
        print(request.query_params) # DRF
        return HttpResponse("APIView GET view v2")

    def post(self, request, *args, **kwargs):
        # print(request.body)
        print(request.POST)  # Django
        print(request.data)  # DRF
        return HttpResponse("APIView POST view v2")

    def put(self, request, *args, **kwargs):
        return HttpResponse("APIView PUT view v2")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("APIView DELETE view v2")


# Content-Type: application/json
class PublishViewV2(APIView):

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


class BookAPIView(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk:
            try:
                instance = Book.objects.get(pk=pk)
            except Book.DoesNotExist as e:
                return Response("{}记录不存在".format(pk))

            s = BookModelSerializer(instance)
        else:
            instances = Book.objects.all()
            s = BookModelSerializer(instances, many=True)
        return Response(s.data)