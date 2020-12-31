from django.shortcuts import HttpResponse, render


# Create your views here.
from django.views.generic import View


def index(request):
    # 相当于controller
    from app01 import models
    ret = models.User.objects.all()  # QuerySet
    print(ret, type(ret))

    for i in ret:
        print(i, i.username, i.password)

    # get 获取不到，或者多条会报错
    one = models.User.objects.get(username='fred')
    print(one.username, one.password)

    filter = models.User.objects.filter(username='fred')
    print(filter)
    return HttpResponse("hello django")


def indexHtml(request):
    # 相当于controller
    return render(request, "index.html")


from django.http.response import JsonResponse

def json(request):
    # 相当于controller
    data = {"k1": "v1"}
    # Content-Type:application/json
    return JsonResponse(data)

class Jsons(View):

    # restful的7种方法
    def get(self, request, num):
        data = {"k1": "get"}
        print('num:', num)
        # Content-Type:application/json
        return JsonResponse(data)

    def post(self, request):
        data = {"k1": "post"}
        # Content-Type:application/json
        return JsonResponse(data)

    def delete(self, request):
        data = {"k1": "delete"}
        # Content-Type:application/json
        return JsonResponse(data)

class Jsons2(View):

    # restful的7种方法
    def get(self, request, age):
        data = {"k1": "get"}
        print('age:', age)
        # Content-Type:application/json
        return JsonResponse(data)