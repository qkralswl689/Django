from pyexpat import model
import re
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from django.views.generic.list import ListView

from .models import Post


def url_view(request):
    data = {'code': '001', 'msg': '0k'}
    # return HttpResponse('url_view')
    return JsonResponse(data)


def url_parameter_view(request, username):
    return HttpResponse(username)


def function_view(request):
    return render(request, 'view.html')


class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'
