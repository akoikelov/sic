from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('static_info/constructor.html', takes_context=True)
def include_si(context):
    if getattr(settings, 'SIC_INCLUDE_JQUERY', False):
        context['sic_include_jquery'] = True
    context['sic_save_btn_lbl'] = getattr(settings, 'SIC_SAVE_BTN_LABEL', 'Save')
    context['sic_textarea_placeholder'] = getattr(settings, 'SIC_TEXTAREA_PLACEHOLDER', 'Put your new content')

    return context


@register.simple_tag(takes_context=True)
def sic_get(context, key, default='Default'):
    data = context['sic_data']

    if data is None or key not in data:
        return default

    return data[key]