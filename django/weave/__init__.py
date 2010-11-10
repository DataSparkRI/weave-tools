def cached_indicator_hierarchy(key_unit_type_id, force_refresh=False):
    from django.template.loader import render_to_string
    from django.core.cache import cache
    from models import Category, Indicator, DataFilter
    
    # We need to find all the top-level categories for this key unit type.
    # Indicators are attached at the bottom of the tree, so start there
    # and walk back up to get the set of top level categories.
    categories = set()
    cats_with_indicators = Category.objects.filter(
            indicators__key_unit_type__id=key_unit_type_id).distinct()
    for cat in cats_with_indicators:
        if not cat.parent:
            categories.add(cat)
        else:
            cat_parent = cat
            while cat_parent.parent:
                cat_parent = cat_parent.parent
            categories.add(cat_parent)
    
    context = {
        'categories': list(categories),
        'orphaned_indicators': Indicator.objects.filter(
            category=None,
            key_unit_type__id=key_unit_type_id),
        'data_filters': DataFilter.objects.filter(key_unit_type__id=key_unit_type_id),
    }
    cache_key = 'weave_indicator_hierarchy_%s' % key_unit_type_id
    
    response = cache.get(cache_key)
    if not response or force_refresh:
        response = render_to_string('weave/indicator_hier.xml', context)
        cache.set(cache_key, response, 60 * 60 * 24 * 365)
    return response

