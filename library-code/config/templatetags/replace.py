from django import template

register = template.Library()


@register.filter
def replace_author(value):
    return value.replace(" ", "+")


@register.filter
def replace_cat(value):
    return value.replace(" / ", "-")
