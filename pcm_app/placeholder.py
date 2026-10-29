from django.http import HttpResponse


def sementara(request, **kwargs):
    return HttpResponse('Halaman ini sedang dikerjakan.')