import json
from json import JSONDecodeError

from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('static_info/constructor.html', takes_context=True)
def include_si(context):
    if getattr(settings, 'SI_INCLUDE_JQUERY', False):
        context['include_jquery'] = True

    return context


@register.simple_tag(takes_context=True)
def sic_get(context, key, default='Default'):
    data = context['sic_data']

    if data is None or key not in data:
        return default

    return data[key]