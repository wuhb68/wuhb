from django.shortcuts import HttpResponse


def fff(request):
    print('aaa')
    return HttpResponse('bbb')


def ggg(request):
    print('ccc')
    return HttpResponse('ddd')


def hhh(request):
    print('ddd')
    return HttpResponse('eee')
