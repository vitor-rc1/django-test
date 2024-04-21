from django.http import HttpResponse


def index(request):
    return HttpResponse("curriculum 42")