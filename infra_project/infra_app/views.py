from django.http import HttpResponse


def index(request):
    return HttpResponse(request)


def second_page(request):
    return HttpResponse(request)
