from django.shortcuts import HttpResponse


def ccc(request):
    print(123)
    return HttpResponse('早上好')


def ddd(requet):
    print(123)
    return HttpResponse(456)


def eee(request):
    print(123)
    return HttpResponse(456)
