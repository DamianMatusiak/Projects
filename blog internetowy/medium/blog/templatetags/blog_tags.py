from django import template

register = template.Library()


@register.filter
def pl_genitiv(word, count):
    if count == 1:
        return word
    if count % 10 in [2, 3, 4]:
        return word + "y"
    else:
        return word + "ów"
