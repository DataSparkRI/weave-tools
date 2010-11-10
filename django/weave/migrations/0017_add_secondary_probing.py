# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'KeyUnitType.secondary_probing_indicator'
        db.add_column('weave_keyunittype', 'secondary_probing_indicator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='key_unit_types_as_secondary_probe', null=True, to=orm['weave.Indicator']), keep_default=False)

        # Changing field 'DataFilter.keys_query'
        db.alter_column('weave_datafilter', 'keys_query', self.gf('django.db.models.fields.TextField')(blank=True))
    
    
    def backwards(self, orm):
        
        # Deleting field 'KeyUnitType.secondary_probing_indicator'
        db.delete_column('weave_keyunittype', 'secondary_probing_indicator_id')

        # Changing field 'DataFilter.keys_query'
        db.alter_column('weave_datafilter', 'keys_query', self.gf('django.db.models.fields.TextField')())
    
    
    models = {
        'weave.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['weave.Category']"})
        },
        'weave.clientconfiguration': {
            'Meta': {'object_name': 'ClientConfiguration'},
            'data_filter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.DataFilter']"}),
            'default_coloring': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'configs_as_color'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'years': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'weave.datafilter': {
            'Meta': {'object_name': 'DataFilter'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_unit_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.KeyUnitType']", 'null': 'True'}),
            'keys_query': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'weave.indicator': {
            'Meta': {'object_name': 'Indicator'},
            'case_restrictions': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicators'", 'null': 'True', 'to': "orm['weave.Category']"}),
            'category_four': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'category_one': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'category_three': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'category_two': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'dataset_tag': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'hover_label': ('django.db.models.fields.TextField', [], {}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_field_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'key_unit_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.KeyUnitType']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_label': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'short_label_prefix': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'table_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_group': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'variable_definition': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        'weave.keyunittype': {
            'Meta': {'object_name': 'KeyUnitType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'probing_indicator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'key_unit_types_as_probe'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'secondary_probing_indicator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'key_unit_types_as_secondary_probe'", 'null': 'True', 'to': "orm['weave.Indicator']"})
        },
        'weave.layout': {
            'Meta': {'object_name': 'Layout'},
            'config_template': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'weave.row': {
            'Meta': {'object_name': 'Row'},
            'config': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rows'", 'to': "orm['weave.ClientConfiguration']"}),
            'height': ('weave.fields.PercentField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'width': ('weave.fields.PercentField', [], {})
        },
        'weave.tool': {
            'Meta': {'object_name': 'Tool'},
            'barChartTitle': ('django.db.models.fields.CharField', [], {'default': "'Bar Chart'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'binAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_bin'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'colorAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_color'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'data_filter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.DataFilter']", 'null': 'True', 'blank': 'True'}),
            'height': ('weave.fields.PercentField', [], {}),
            'heightAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_height'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'histogramTitle': ('django.db.models.fields.CharField', [], {'default': "'Histogram'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapTitle': ('django.db.models.fields.CharField', [], {'default': "'Rhode Island'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'row': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tools'", 'to': "orm['weave.Row']"}),
            'sortingAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_sorting'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'table_columns': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tools_as_table_column'", 'blank': 'True', 'to': "orm['weave.Indicator']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'width': ('weave.fields.PercentField', [], {}),
            'xAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_x'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'yAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_y'", 'null': 'True', 'to': "orm['weave.Indicator']"})
        }
    }
    
    complete_apps = ['weave']
