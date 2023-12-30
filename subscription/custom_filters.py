from django import template

register = template.Library()

@register.filter(name='split_by_comma')
def split_by_comma(value):
    if value:
        return value.split(',')
    return []
