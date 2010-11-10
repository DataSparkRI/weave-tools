
from south.db import db
from django.db import models
from webportal.weave.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'ClientConfiguration.default_coloring'
        db.add_column('weave_clientconfiguration', 'default_coloring', orm['weave.clientconfiguration:default_coloring'])
        
        # Changing field 'Row.order'
        # (to signature: django.db.models.fields.PositiveIntegerField())
        db.alter_column('weave_row', 'order', orm['weave.row:order'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'ClientConfiguration.default_coloring'
        db.delete_column('weave_clientconfiguration', 'default_coloring_id')
        
        # Changing field 'Row.order'
        # (to signature: django.db.models.fields.PositiveIntegerField(default=1))
        db.alter_column('weave_row', 'order', orm['weave.row:order'])
        
    
    
    models = {
        'weave.clientconfiguration': {
            'dataTable': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.DataTable']"}),
            'default_coloring': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'configs_as_color'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'weave.datatable': {
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keys_query': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'weave.indicator': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_field_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'table_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'weave.layout': {
            'config_template': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'weave.row': {
            'config': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rows'", 'to': "orm['weave.ClientConfiguration']"}),
            'height': ('PercentField', [], {'default': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'width': ('PercentField', [], {'default': '100'})
        },
        'weave.tool': {
            'barChartTitle': ('django.db.models.fields.CharField', [], {'default': "'Bar Chart'", 'max_length': '100'}),
            'binAttribute': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tools_as_bin'", 'to': "orm['weave.Indicator']"}),
            'colorAttribute': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tools_as_color'", 'to': "orm['weave.Indicator']"}),
            'height': ('PercentField', [], {'default': '100'}),
            'heightAttribute': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tools_as_height'", 'to': "orm['weave.Indicator']"}),
            'histogramTitle': ('django.db.models.fields.CharField', [], {'default': "'Histogram'", 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapTitle': ('django.db.models.fields.CharField', [], {'default': "'Rhode Island'", 'max_length': '100'}),
            'row': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tools'", 'to': "orm['weave.Row']"}),
            'sortingAttribute': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tools_as_sorting'", 'to': "orm['weave.Indicator']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'width': ('PercentField', [], {'default': '100'}),
            'xAttribute': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tools_as_x'", 'to': "orm['weave.Indicator']"}),
            'yAttribute': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tools_as_y'", 'to': "orm['weave.Indicator']"})
        }
    }
    
    complete_apps = ['weave']
