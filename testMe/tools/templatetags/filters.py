from django import template
register = template.Library()

@register.filter(name='times')
def times(number_str):
    number = int(number_str)
    return range(number)