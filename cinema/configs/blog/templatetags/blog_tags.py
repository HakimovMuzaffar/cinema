from django import template
from ..models import *

register = template.Library()


@register.simple_tag()
def get_sorters():
    sorters = {
        '-view': 'View ⬆️',
        'view': 'View ⬇️',
        'title': 'A - Z',
        '-title': 'Z - A',
        '-created_at': 'Old cinema',
        'created_at': 'New cinema'
    }
    return sorters
