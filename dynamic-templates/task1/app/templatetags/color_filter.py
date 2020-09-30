from django.template import library


register = library.Library()

@register.filter
def get_color(value):
    if value == '':
        return 'white'
    elif float(value) < 0:
        return 'green'
    elif 1 <= float(value) < 2:
        return 'pink'
    elif 2 <= float(value) < 5:
        return 'crimson'
    elif float(value) >= 5:
        return 'red'
    else:
        return 'white'

@register.filter
def replace_emptiness(value):
    if value == '':
        return '-'
    else:
        return value