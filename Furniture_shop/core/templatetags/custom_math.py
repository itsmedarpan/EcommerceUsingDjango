from django import template

register = template.Library()

@register.filter
def subtract(value, arg):
    """Subtracts arg from value"""
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        return ''
