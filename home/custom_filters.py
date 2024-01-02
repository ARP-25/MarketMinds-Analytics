from django import template
from subscription.models import SubscriptionPlan


register = template.Library()

@register.filter
def get_by_id(queryset, id):
    return queryset.filter(id=id).first()


@register.filter(name='split_by_comma')
def split_by_comma(value):
    if value:
        return value.split(',')
    return []


