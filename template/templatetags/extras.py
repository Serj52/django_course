from django import template

register = template.Library()

@register.filter
def inc(a, b):
    res = int(a) + int(b)
    return res

@register.simple_tag
def division(a, b, to_int = False):
    res = int(a)/int(b)
    if to_int == True:
        return int(res)
    else:
        return res