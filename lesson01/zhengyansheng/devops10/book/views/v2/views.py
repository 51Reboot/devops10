from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse

from book.models import Publisher
from book.views.v2.serialization import PublisherSerializer


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
        # print(request.GET)  # Django
        # print(request.query_params) # DRF
        ps = Publisher.objects.all()
        s = PublisherSerializer(ps, many=True)
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
            return Response("提交数据成功.")
        else:
            return Response(s.error_messages)
        # return HttpResponse("APIView POST view v2")

    def put(self, request, *args, **kwargs):
        return HttpResponse("APIView PUT view v2")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("APIView DELETE view v2")