from django import template


register = template.Library()


@register.inclusion_tag('static_info/js.html', takes_context=True)
def include_si(context):
    return context