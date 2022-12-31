from django import template
register = template.Library()

@register.filter(name="addcss")
def addcss(field, css_class):
    '''Add css class to a form field'''

    attrs = {
            'class': css_class,
            }
    return field.as_widget(attrs=attrs)

@register.filter(name='addcssid')
def addcssid(field, css_id):
    '''Adds css id to the form field'''

    attrs = {
            'id': css_id,
            }
    return field.as_widget(attrs=attrs)
