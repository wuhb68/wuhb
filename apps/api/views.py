from django.shortcuts import HttpResponse


def index(request):
    print('早上好啊')
    return HttpResponse('早上好')


def aaa(request):
    print('中午好啊')
    return HttpResponse('中午好')


def bbb(request):
    print('晚上好啊')
    return HttpResponse('晚上好')
