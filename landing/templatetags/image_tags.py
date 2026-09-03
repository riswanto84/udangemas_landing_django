from django import template

register = template.Library()


@register.filter
def optimized_image(image):
    if not image:
        return ""

    name = image.name

    if "." in name:
        name = name.rsplit(".", 1)[0]

    return f"/media/optimized/{name}.webp"
