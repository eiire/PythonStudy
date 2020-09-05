from django.shortcuts import render
from django.http import HttpResponse


# (HTML) Обращение к ключам словаря, списка и кортежа через '.' (аналогично для методов)
def echo(request):
    method = 'default_method'
    context_for_var = {}
    context_for_meta = {}
    # print(request.GET)  # <QueryDict: {'a': ['1'], 'v': ['3']}>
    if request.method == 'GET':
        method = 'get'
        context_for_var.update({'check': 0})
        for k, v in request.GET.items():
            context_for_var.update({'check': '1'})  # проверка на отсутствие ключей, чтобы вывести только заголовок
            context_for_var.update({k: v[0]})
    elif request.method == 'POST':
        method = 'post'
        for k, v in request.POST.items():
            context_for_var.update({'check': '1'})
            context_for_var.update({k: v[0]})

    for k, v in request.META.items():
        context_for_meta.update({k: v})  # v is not list
        if k == 'HTTP_X_PRINT_STATEMENT':
            context_for_meta.update({'HTTP_X_PRINT_STATEMENT': v})
        else:
            context_for_meta.update({'HTTP_X_PRINT_STATEMENT': 'empty'})

    # контекст состоит из словаря, по ключам могут хранится другие типы данных
    data = {'method': method, 'dict_var': context_for_var, 'dict_headers': context_for_meta}

    # print(context_for_var)
    return HttpResponse(status=200, content=render(request, 'echo.html', context=data))


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
