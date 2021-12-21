from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_POST, require_GET
import re


def simple_route(request):
    if request.method == 'GET':
        if str(request.path) == '/routing/simple_route/':
            return HttpResponse(status='200')
        elif str(request.path) == re.findall(r'/routing/simple_route/\w+.*', str(request.path))[0]:
            return HttpResponse(status='404')
    elif request.method == 'POST' or request.method == 'PUT':
        return HttpResponse(status='405')


def slug_route(request, page_slug=None):
    if page_slug != None and (1 <= len(page_slug) <= 16) and (
            page_slug == re.findall(r'(?:[0-9]*-*_*[a-z]*-*_*[0-9]*)*', page_slug)[0]):
        return HttpResponse(content=page_slug)
    else:
        return HttpResponse(status='404')


def sum_route(request, a, b):
    try:
        res = int(a) + int(b)
        return HttpResponse(content=res, status='200')
    except ValueError:
        return HttpResponse(status='404')


@require_GET
def sum_get_method(request):
    try:
        res = int(request.GET.get('a')) + int(request.GET.get('b'))
        return HttpResponse(content=res, status='200')
    except ValueError:
        return HttpResponse(status='400')
    except TypeError:
        return HttpResponse(status='400')

@require_POST
def sum_post_method(request):
    try:
        res = int(request.POST.get('a')) + int(request.POST.get('b'))
        return HttpResponse(content=res, status='200')
    except ValueError:
        return HttpResponse(status='400')
    except TypeError:
        return HttpResponse(status='400')

# Create your views here.
