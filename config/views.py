from django.http import HttpResponse, response


def index(request):
    return HttpResponse("hello","Test")