from django import template

register = template.Library()

@register.simple_tag(name='mediapath')
def media_tag(text):
    return f'/media/{text}'

@register.filter(name='mediapath')
def media_filter(text):
    return f'/media/{text}'