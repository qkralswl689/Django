import re
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse


def url_view(request):
    data = {'code': '001', 'msg': '0k'}
    # return HttpResponse('url_view')
    return JsonResponse(data)


def url_parameter_view(request, username):
    return HttpResponse(username)
