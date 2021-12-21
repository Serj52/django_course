from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_POST, require_GET
import re

def echo(request):
    head = request.META.get('HTTP_X_PRINT_STATEMENT', 'empty')
    if request.method == 'GET':
        if request.GET:
            return render(request, 'echo.html', status='200',
                          context={'param': request.GET, 'head': head, 'method': 'get'})
        else:
            return render(request, 'echo.html', status='200', context={'head': head})

    elif request.method == 'POST':
        if request.POST:
            return render(request, 'echo.html', status='200',
                          context={'param': request.POST, 'head': head, 'method': 'post'})
        else:
            return render(request, 'echo.html', status='200', context={'head': head})


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', '10'),
        'b': request.GET.get('b', '3')
    })

def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })