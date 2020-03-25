#  https://djbook.ru/rel1.8/howto/custom-template-tags.html - templates
from django import template
register = template.Library()


@ register.filter(name='inc')
def inc(arg_1, arg_2):
    res = int(arg_1) + int(arg_2)
    return str(res)


@ register.simple_tag
def division(*args, **kwargs):
    try:
        if kwargs['to_int']:
            return int(int(args[0]) / int(args[1]))
        else:
            return float(float(args[0]) / float(args[1]))
    except KeyError:
        return float(float(args[0]) / float(args[1]))