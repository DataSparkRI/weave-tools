from django.db.models.fields import IntegerField
from south.modelsinspector import add_introspection_rules
from django.db.models.fields import NOT_PROVIDED
from django.conf import settings

class PercentField(IntegerField):
#    def get_internal_type(self):
#        return "IntegerField"
    
    def formfield(self, **kwargs):
        defaults = {'min_value': 0}
        defaults = {'max_value': 100}
        defaults.update(kwargs)
        return super(PercentField, self).formfield(**defaults)

rules = [(
            (PercentField, ),
	        [],
	        {
	            "null": ["null", {"default": False}],
	            "blank": ["blank", {"default": False, "ignore_if":"primary_key"}],
	            "primary_key": ["primary_key", {"default": False}],
	            "max_length": ["max_length", {"default": None}],
	            "unique": ["_unique", {"default": False}],
	            "db_index": ["db_index", {"default": False}],
	            "default": ["default", {"default": 100}],
	            "db_column": ["db_column", {"default": None}],
	            "db_tablespace": ["db_tablespace", {"default": settings.DEFAULT_INDEX_TABLESPACE}],
	        },
	      ),]

add_introspection_rules(rules=rules, patterns=['weave\.fields\.'])

