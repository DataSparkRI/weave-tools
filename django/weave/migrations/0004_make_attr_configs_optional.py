
from south.db import db
from django.db import models
from webportal.weave.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Tool.colorAttribute'
        # (to signature: django.db.models.fields.related.ForeignKey(blank=True, null=True, to=orm['weave.Indicator']))
        db.alter_column('weave_tool', 'colorAttribute_id', orm['weave.tool:colorAttribute'])
        
        # Changing field 'Tool.histogramTitle'
        # (to signature: django.db.models.fields.CharField(default='Histogram', max_length=100, null=True, blank=True))
        db.alter_column('weave_tool', 'histogramTitle', orm['weave.tool:histogramTitle'])
        
        # Changing field 'Tool.yAttribute'
        # (to signature: django.db.models.fields.related.ForeignKey(blank=True, null=True, to=orm['weave.Indicator']))
        db.alter_column('weave_tool', 'yAttribute_id', orm['weave.tool:yAttribute'])
        
        # Changing field 'Tool.mapTitle'
        # (to signature: django.db.models.fields.CharField(default='Rhode Island', max_length=100, null=True, blank=True))
        db.alter_column('weave_tool', 'mapTitle', orm['weave.tool:mapTitle'])
        
        # Changing field 'Tool.heightAttribute'
        # (to signature: django.db.models.fields.related.ForeignKey(blank=True, null=True, to=orm['weave.Indicator']))
        db.alter_column('weave_tool', 'heightAttribute_id', orm['weave.tool:heightAttribute'])
        
        # Changing field 'Tool.binAttribute'
        # (to signature: django.db.models.fields.related.ForeignKey(blank=True, null=True, to=orm['weave.Indicator']))
        db.alter_column('weave_tool', 'binAttribute_id', orm['weave.tool:binAttribute'])
        
        # Changing field 'Tool.xAttribute'
        # (to signature: django.db.models.fields.related.ForeignKey(blank=True, null=True, to=orm['weave.Indicator']))
        db.alter_column('weave_tool', 'xAttribute_id', orm['weave.tool:xAttribute'])
        
        # Changing field 'Tool.barChartTitle'
        # (to signature: django.db.models.fields.CharField(default='Bar Chart', max_length=100, null=True, blank=True))
        db.alter_column('weave_tool', 'barChartTitle', orm['weave.tool:barChartTitle'])
        
        # Changing field 'Tool.sortingAttribute'
        # (to signature: django.db.models.fields.related.ForeignKey(blank=True, null=True, to=orm['weave.Indicator']))
        db.alter_column('weave_tool', 'sortingAttribute_id', orm['weave.tool:sortingAttribute'])
        
    
    
    def backwards(self, orm):
        
        # Changing field 'Tool.colorAttribute'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['weave.Indicator']))
        db.alter_column('weave_tool', 'colorAttribute_id', orm['weave.tool:colorAttribute'])
        
        # Changing field 'Tool.histogramTitle'
        # (to signature: django.db.models.fields.CharField(default='Histogram', max_length=100))
        db.alter_column('weave_tool', 'histogramTitle', orm['weave.tool:histogramTitle'])
        
        # Changing field 'Tool.yAttribute'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['weave.Indicator']))
        db.alter_column('weave_tool', 'yAttribute_id', orm['weave.tool:yAttribute'])
        
        # Changing field 'Tool.mapTitle'
        # (to signature: django.db.models.fields.CharField(default='Rhode Island', max_length=100))
        db.alter_column('weave_tool', 'mapTitle', orm['weave.tool:mapTitle'])
        
        # Changing field 'Tool.heightAttribute'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['weave.Indicator']))
        db.alter_column('weave_tool', 'heightAttribute_id', orm['weave.tool:heightAttribute'])
        
        # Changing field 'Tool.binAttribute'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['weave.Indicator']))
        db.alter_column('weave_tool', 'binAttribute_id', orm['weave.tool:binAttribute'])
        
        # Changing field 'Tool.xAttribute'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['weave.Indicator']))
        db.alter_column('weave_tool', 'xAttribute_id', orm['weave.tool:xAttribute'])
        
        # Changing field 'Tool.barChartTitle'
        # (to signature: django.db.models.fields.CharField(default='Bar Chart', max_length=100))
        db.alter_column('weave_tool', 'barChartTitle', orm['weave.tool:barChartTitle'])
        
        # Changing field 'Tool.sortingAttribute'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['weave.Indicator']))
        db.alter_column('weave_tool', 'sortingAttribute_id', orm['weave.tool:sortingAttribute'])
        
    
    
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
            'barChartTitle': ('django.db.models.fields.CharField', [], {'default': "'Bar Chart'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'binAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_bin'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'colorAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_color'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'height': ('PercentField', [], {'default': '100'}),
            'heightAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_height'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'histogramTitle': ('django.db.models.fields.CharField', [], {'default': "'Histogram'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapTitle': ('django.db.models.fields.CharField', [], {'default': "'Rhode Island'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'row': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tools'", 'to': "orm['weave.Row']"}),
            'sortingAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_sorting'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'width': ('PercentField', [], {'default': '100'}),
            'xAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_x'", 'null': 'True', 'to': "orm['weave.Indicator']"}),
            'yAttribute': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tools_as_y'", 'null': 'True', 'to': "orm['weave.Indicator']"})
        }
    }
    
    complete_apps = ['weave']
