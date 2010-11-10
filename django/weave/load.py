import re
from xml.sax.saxutils import quoteattr

from django.db import IntegrityError  
from django.contrib.contenttypes.models import ContentType

from indicators.models import Indicator, IndicatorData
from weave.models import DataTable, KeyUnitType, AttributeColumn, DataFilter

def time_translations(input):
    if not input:
        return None
    
    # school years
    sy_re = re.compile(r'School Year [0-9]{2}(?P<start_year>[0-9]{2})-[0-9]{2}(?P<end_year>[0-9]{2})')
    
    sy_match = sy_re.match(input)
    if sy_match:
        return 'SY%s-%s' % (sy_match.group('start_year'), 
            sy_match.group('end_year'))

    # Calendar Years
    cy_re = re.compile(r'Calendar Year (?P<year>[0-9]{4})')

    cy_match = cy_re.match(input)
    if cy_match:
        return '%s' % cy_match.group('year')
    
    # future conversions...

    return input

def run():
    indicator_ctype = ContentType.objects.get(app_label='indicators', model='indicator')
    
    # set up Data Tables
    DataTable.objects.all().delete()
    datatable_cache = {}
    for key_unit_type in IndicatorData.objects.values_list('key_unit_type',flat=True).distinct():
        data_table, created = DataTable.objects.get_or_create(name=key_unit_type, key_unit_type=key_unit_type)
        datatable_cache[key_unit_type] = data_table
        key_unit_type, created = KeyUnitType.objects.get_or_create(name=key_unit_type)
    
    # create AttributeColumns
    for indicator in Indicator.objects.all().iterator():
        for indicator_data in indicator.indicatordata_set.values(
                'key_unit_type', 'time_key', 'data_type', 'time_type').distinct():
            try:
                if indicator.data_type.upper() == 'NUMERIC':
                    data_type = 'number'
                    sql_type = 'numeric'
                else:
                    data_type = 'text'
                    sql_type = 'string'

                if indicator_data['time_type'] and indicator_data['time_key']:
                    time = "%s %s" % (indicator_data['time_type'], indicator_data['time_key'])
                else:
                    time = indicator_data['time_key']
                if not indicator_data['time_key'] or indicator_data['time_key'].strip() == '':
                    time_sql = 'indicators_indicatordata."time_key" is null'
                else:
                    time_sql = 'indicators_indicatordata."time_key" = \'%s\' and indicators_indicatordata."time_type" = \'%s\'' % (indicator_data['time_key'], indicator_data['time_type'])
                data_with_keys_query = """
                    SELECT key_value, %s from indicators_indicatordata WHERE indicators_indicatordata."indicator_id" = '%s' AND indicators_indicatordata."key_unit_type" like '%s' AND (%s)
                """ % (
                    sql_type,
                    indicator.id,
                    indicator_data['key_unit_type'],
                    time_sql,
                )
                
                attribute_column, created = AttributeColumn.objects.get_or_create(
                    content_type=indicator_ctype,
                    object_id=indicator.id,
                    data_table=datatable_cache[indicator_data['key_unit_type']],
                    name=indicator.name,
                    display_name=indicator.weave_name(),
                    category=None,
                    key_unit_type=indicator_data['key_unit_type'],
                    year=time_translations(time) or '',
                    data_type=data_type,
                    data_with_keys_query=data_with_keys_query.strip(),
                    min=indicator.min,
                    max=indicator.max
                )
            except IntegrityError:
                print "Duplicate AttributeColumn detected for (%s, %s, %s). AttributeColumn NOT created." % (
                    indicator.name,
                    indicator.key_unit_type,
                    indicator_data['time_key']
                )
    
    for data_table in DataTable.objects.all():
        key_unit_type = KeyUnitType.objects.get(name=data_table.key_unit_type)
        for data_filter in DataFilter.objects.filter(key_unit_type=key_unit_type):
            filtered_data_table, created = DataTable.objects.get_or_create_for_filter(data_filter)
            for attribute_column in data_table.attributecolumn_set.all():
                attribute_column, created = AttributeColumn.objects.get_or_create(
                    content_type=attribute_column.content_type,
                    object_id=attribute_column.object_id,
                    data_table=filtered_data_table,
                    name=attribute_column.name,
                    display_name=attribute_column.display_name,
                    category=None,
                    key_unit_type=attribute_column.key_unit_type,
                    year=attribute_column.year,
                    data_type=attribute_column.data_type,
                    data_with_keys_query=data_filter.modify_query(attribute_column.data_with_keys_query),
                    min=attribute_column.min,
                    max=attribute_column.max
                )
                     

    # TODO: update min/max where possible and not already specified
