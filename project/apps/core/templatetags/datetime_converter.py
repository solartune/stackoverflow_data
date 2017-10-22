from datetime import datetime

from django import template

register = template.Library()


@register.filter
def fromtimestamp(value):
    """Convert timestamp (unix time) to datetime format."""
    try:
        return datetime.fromtimestamp(int(value))
    except:
        return value
