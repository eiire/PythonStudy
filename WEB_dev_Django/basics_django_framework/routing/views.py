from django.http import HttpResponse


# Метод	Путь	Статус	Тело
# get	/routing/simple_route/	200	Пустое
# get	/routing/simple_route/blabla	404	-
# post	/routing/simple_route/	405	-
# put	/routing/simple_route/	405	-
def simple_route(request):
    if "/routing/simple_route/" != str(request.path):
        return HttpResponse(status=404)

    if request.method == 'GET':
        return HttpResponse(content='', status=200)
    else:
        return HttpResponse(status=405)


# get	/routing/slug_route/a-1s_d2/	200	a-1s_d2
# get	/routing/slug_route/1411rwasf123412341234/	404	-
# get	/routing/slug_route/.4/24][/	404	-
def slug_route(request, slug):
    return HttpResponse(content=slug)


# get	/routing/sum_route/1/2/	200	3
# get	/routing/sum_route/1/-2/	200	-1
# get	/routing/sum_route/1/b/	404	-
# get	/routing/sum_route/a/2/	404	-
def sum_route(request, var_1, var_2):
    return HttpResponse(content=int(var_1) + int(var_2))


# get	/routing/sum_get_method/?a=1&b=2	200	3
# get	/routing/sum_get_method/?a=1&b=-2	200	-1
# get	/routing/sum_get_method/?a=1&b=b	400	-
# get	/routing/sum_get_method/?a=a&b=2	400	-
# get	/routing/sum_get_method/	400	-
def get_sum_route(request):
    if request.method != 'GET':
        return HttpResponse(status=405)

    var_1 = request.GET.get("a", "bad")
    var_2 = request.GET.get("b", "bad")
    return correct_response(var_1, var_2)


# /routing/sum_post_method/	a=1&b=2	200	3
# /routing/sum_post_method/	a=1&b=-2	200	-1
# /routing/sum_post_method/	a=1&b=b	400	-
# /routing/sum_post_method/	a=a&b=2	400	-
# /routing/sum_post_method/	-	400	-
def sum_post_method(request):
    if request.method != 'POST':
        return HttpResponse(status=405)

    var_1 = request.POST.get("a", "bad")
    var_2 = request.POST.get("b", "bad")
    return correct_response(var_1, var_2)


def correct_response(var_1, var_2):
    if is_digit(var_1) != True or is_digit(var_2) != True:
        return HttpResponse(content='', status=400)
    else:
        return HttpResponse(content=str(int(var_1) + int(var_2)))


def is_digit(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
