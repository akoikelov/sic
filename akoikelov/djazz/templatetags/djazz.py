from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('static_info/constructor.html', takes_context=True)
def include_si(context):
    if getattr(settings, 'SI_INCLUDE_JQUERY', False):
        context['include_jquery'] = True

    return context