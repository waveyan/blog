from ..models import Url,Sentence
from django import template

register=template.Library()

@register.simple_tag
def get_urls(num=6):
    return Url.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def get_sentence():
    return Sentence.objects.latest('id')
