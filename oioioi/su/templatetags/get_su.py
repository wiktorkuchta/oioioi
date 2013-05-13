from django import template


register = template.Library()

@register.inclusion_tag('su/dropdown-form.html', takes_context=True)
def su_dropdown_form(context):
    from oioioi.su.forms import SuForm
    from oioioi.su.utils import is_under_su

    return {
        'ctx': context,
        'form': SuForm(auto_id='su-%s'),
        'is_under_su': is_under_su(context['request']),
    }