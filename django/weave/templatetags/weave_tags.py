from xml.sax.saxutils import escape
from xml.sax.saxutils import quoteattr as sax_quoteattr

from django import template
from django.template.defaultfilters import stringfilter

from weave.models import AttributeColumn

register = template.Library()


@register.simple_tag
def indicator_name(indicator, data_filter):
    return escape(data_filter.indicator_name(indicator))

@register.inclusion_tag('weave/category_display.xml')
def category_display(category, data_filter):
    return {'category': category, 'data_filter': data_filter}

@register.filter
@stringfilter
def quoteattr(value):
    return sax_quoteattr(value)

@register.filter
def filter_for_attr_list_Q(originalqueryset, attributecolumn_Q=None):
    return originalqueryset.filter(attributecolumn_Q)

@register.inclusion_tag('weave/attributecolumn_list_hierarchy.xml')
def attributecolumn_list_hierarchy(hierarchy_name, attributecolumn_Q):
    """
    Takes a Q object defining the attribute columns to be displayed by this
    hierarchy and constructs an appropriate XML fragment, sliced by KeyUnitType
    and any applicable DataFilters.
    
    Please note that this is a Q, you can't pass a list or QuerySet here or the
    tag will fail as currently written.
    """
    key_unit_types = KeyUnitType.objects.filter(
        name__in=AttributeColumn.objects.filter(attributecolumn_Q).order_by(
            'year').values_list('key_unit_type', flat=True).distinct()
    )
    return {
        'hierarchy_name': hierarchy_name, 
        'list_Q': attributecolumn_Q,
        'key_unit_types': key_unit_types
    }
