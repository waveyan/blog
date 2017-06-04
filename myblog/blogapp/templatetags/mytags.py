from ..models import Url
from django import template

register=template.Library()

@register.simple_tag
def get_urls(num=6):
    return Url.objects.all().order_by('-created_time')[:num]
