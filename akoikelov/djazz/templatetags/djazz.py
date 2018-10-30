from django import template


register = template.Library()


@register.inclusion_tag('static_info/js.html')
def include_si():
    return {}