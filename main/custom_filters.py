from django import template
import re

register = template.Library()

@register.filter(name='make_links_clickable')
def make_links_clickable(value):
    return re.sub(r'(https?://\S+)', r'<a href="\1" target="_blank">\1</a>', value)
