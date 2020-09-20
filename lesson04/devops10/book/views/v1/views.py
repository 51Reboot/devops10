import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import Http404
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from book.models import Publisher

@csrf_exempt
def PublishView(request, *args, **kwargs):
    # print(dir(request))
    print(request.method)

    if request.method == 'GET':
        return HttpResponse("GET")

    elif request.method == 'POST':
        return HttpResponse("POST")

    elif request.method == 'PUT':
        return HttpResponse("PUT")

    elif request.method == 'DELETE':
        return HttpResponse("DELETE")
    else:
        raise Http404()


class PublishViewV2(View):

    def get(self, request, *args, **kwargs):
        print(request.GET)
        return HttpResponse("GET view v2")

    def post(self, request, *args, **kwargs):
        # print(request.body)
        print(request.POST)
        return HttpResponse("POST view v2")

    def put(self, request, *args, **kwargs):
        return HttpResponse("PUT view v2")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("DELETE view v2")


retdata = {
    "code": 0,
    "data": None,
    "message": "",
    "request_id": "",
}


# GET 全部
# GET 单个数据
# POST
# PUT
# DELETE

class PublisherViewV3(View):

    def get_object(self, pk):
        try:
            obj = Publisher.objects.get(pk=pk)
        except Publisher.DoesNotExist as e:
            raise Http404()
        return obj

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            obj = self.get_object(pk)
            _data_dict = {
                "pk": obj.pk,
                "name": obj.name,
                "address": obj.address,
            }
            retdata['data'] = _data_dict
            return JsonResponse(retdata)
        else:
            objs = Publisher.objects.all()
            _data_list = []
            for obj in objs:
                _data_list.append({
                    "pk": obj.pk,
                    "name": obj.name,
                    "address": obj.address,
                })
            retdata["data"] = _data_list
            return JsonResponse(retdata, safe=False)

    def post(self, request, *args, **kwargs):
        if request.content_type == 'application/json':
            data = request.body
            try:
                data = json.loads(data)
            except Exception as e:
                retdata['code'] = -1
                retdata['message'] = e
                return JsonResponse(retdata)
        elif request.content_type == 'application/x-www-form-urlencoded':
            data = request.POST.dict()
        else:
            retdata['code'] = -1
            retdata['data'] = ""
            retdata['message'] = "Content-Type不支持当前"
            return JsonResponse(retdata)
        try:
            p = Publisher.objects.create(**data)
        except Exception as e:
            retdata['code'] = -1
            retdata['message'] = "Publisher create err {}".format(e)
            return JsonResponse(retdata)
        else:
            data['pk'] = p.pk
            retdata["data"] = data
            return JsonResponse(retdata)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.get_object(pk)
        if request.content_type == 'application/json':
            data = request.body
            try:
                data = json.loads(data)
            except Exception as e:
                retdata['code'] = -1
                retdata['message'] = e
                return JsonResponse(retdata)
        elif request.content_type == 'application/x-www-form-urlencoded':
            data = request.POST.dict()
        else:
            retdata['code'] = -1
            retdata['message'] = "Content-Type不支持当前"
            return JsonResponse(retdata)

        try:
            Publisher.objects.filter(pk=pk).update(**data)
        except Exception as e:
            retdata['code'] = -1
            retdata['message'] = 'Update pk {} err {}.'.format(pk, e)
            return JsonResponse(retdata)
        else:
            return JsonResponse(retdata)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.get_object(pk)

        try:
            Publisher.objects.get(pk=pk).delete()
        except Exception as e:
            retdata['code'] = -1
            retdata['message'] = 'Delete pk {} err {}.'.format(pk, e)
            return JsonResponse(retdata)
        else:
            return JsonResponse(retdata)















