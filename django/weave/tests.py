from django.test import TestCase

class BugFixTests(TestCase):
    def test_381(self):
        """ 
        Newly created DataFilters are crashing a user's indicator hierarchy
        """
        from weave.models import DataFilter, KeyUnitType, AttributeColumn, DataTable
        try:
            data_filter = DataFilter.objects.create(
                name='Test', 
                key_unit_type=KeyUnitType.objects.create(name='Test'),
            )
        except ValueError:
            pass
        data_table = DataTable.objects.create(
            name='Test',
            key_unit_type='Test'
        )

        attribute_column = AttributeColumn.objects.create(
            data_table = data_table,
            name='test',
            display_name='test',
            key_unit_type='Test',
            data_type='string',
        )
        
        self.failUnlessEqual(
            self.client.get('/indicators/list_hierarchy/default.xml').status_code,
            200
        )

class TimeTranslationTest(TestCase):
    def test_school_year(self):
        """
        Tests that "School Year 2005-2006" gets turned into "SY05-06" in weave.
        """
        from indicators.models import Indicator, IndicatorData
        from weave.load import run
        from weave.models import AttributeColumn
        
        i = Indicator.objects.create(
            name='test',
            display_name='test'
        )
        IndicatorData.objects.create(indicator=i, time_type='School Year', time_key = "2005-2006", key_unit_type = "School", key_value = "00001", data_type = 'numeric', numeric = 100)
        
        run()

        self.failUnlessEqual(AttributeColumn.objects.all().count(), 1)
        self.failUnlessEqual(AttributeColumn.objects.all()[0].year, 'SY05-06')

    def test_calendar_year(self):
        """
        Tests that "Calendar Year 2005" gets turned into "2005" in weave.
        """
        from indicators.models import Indicator, IndicatorData
        from weave.load import run
        from weave.models import AttributeColumn
        
        i = Indicator.objects.create(
            name='test',
            display_name='test'
        )
        IndicatorData.objects.create(indicator=i, time_type='Calendar Year', time_key = "2005", key_unit_type = "School", key_value = "00001", data_type = 'numeric', numeric = 100)
        
        run()

        self.failUnlessEqual(AttributeColumn.objects.all().count(), 1)
        self.failUnlessEqual(AttributeColumn.objects.all()[0].year, '2005')

    def test_blank_time_type(self):
        """
        Tests that blank time types can pass through type conversion.
        """
        from indicators.models import Indicator, IndicatorData
        from weave.load import run
        from weave.models import AttributeColumn
        
        i = Indicator.objects.create(
            name='test',
            display_name='test'
        )
        IndicatorData.objects.create(indicator=i, time_type=None, time_key = None, key_unit_type = "School", key_value = "00001", data_type = 'numeric', numeric = 100)
        
        run()

        self.failUnlessEqual(AttributeColumn.objects.all().count(), 1)
        self.failUnlessEqual(AttributeColumn.objects.all()[0].year, '')

class DataFilterTest(TestCase):
    fixtures = ['data_filters.json', ]
    def test_display(self):
        """ 
        Test that only DataFilters set to `display` show up for a normal user
        """
        from django.template.loader import render_to_string
        from weave.models import KeyUnitType, AttributeColumn, DataTable, DataFilter
        from django.db.models import Q
        #key_unit_type = KeyUnitType.objects.create(name='School')
        #data_filter = DataFilter.objects.all(
        context = {
            'hierarchy_name': 'test', 
            'list_Q': Q(),
            'key_unit_types': KeyUnitType.objects.all()
        }
        df = DataFilter.objects.all()[0]
        self.failUnless('<category name="%s">' % df.name in render_to_string('weave/attributecolumn_list_hierarchy.xml', context))
        df.display = False
        df.save()
        self.failUnless('<category name="%s">' % df.name not in render_to_string('weave/attributecolumn_list_hierarchy.xml', context))
