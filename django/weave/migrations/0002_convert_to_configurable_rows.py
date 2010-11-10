
from south.db import db
from django.db import models
from webportal.weave.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Tool'
        db.create_table('weave_tool', (
            ('yAttribute', orm['weave.tool:yAttribute']),
            ('histogramTitle', orm['weave.tool:histogramTitle']),
            ('colorAttribute', orm['weave.tool:colorAttribute']),
            ('mapTitle', orm['weave.tool:mapTitle']),
            ('binAttribute', orm['weave.tool:binAttribute']),
            ('height', orm['weave.tool:height']),
            ('width', orm['weave.tool:width']),
            ('xAttribute', orm['weave.tool:xAttribute']),
            ('heightAttribute', orm['weave.tool:heightAttribute']),
            ('barChartTitle', orm['weave.tool:barChartTitle']),
            ('sortingAttribute', orm['weave.tool:sortingAttribute']),
            ('type', orm['weave.tool:type']),
            ('id', orm['weave.tool:id']),
            ('row', orm['weave.tool:row']),
        ))
        db.send_create_signal('weave', ['Tool'])
        
        # Adding model 'Row'
        db.create_table('weave_row', (
            ('width', orm['weave.row:width']),
            ('order', orm['weave.row:order']),
            ('config', orm['weave.row:config']),
            ('id', orm['weave.row:id']),
            ('height', orm['weave.row:height']),
        ))
        db.send_create_signal('weave', ['Row'])
        
        # Deleting field 'ClientConfiguration.histogramTitle'
        db.delete_column('weave_clientconfiguration', 'histogramTitle')
        
        # Deleting field 'ClientConfiguration.barChartTitle'
        db.delete_column('weave_clientconfiguration', 'barChartTitle')
        
        # Deleting field 'ClientConfiguration.yAttribute'
        db.delete_column('weave_clientconfiguration', 'yAttribute_id')
        
        # Deleting field 'ClientConfiguration.heightAttribute'
        db.delete_column('weave_clientconfiguration', 'heightAttribute_id')
        
        # Deleting field 'ClientConfiguration.sortingAttribute'
        db.delete_column('weave_clientconfiguration', 'sortingAttribute_id')
        
        # Deleting field 'ClientConfiguration.xAttribute'
        db.delete_column('weave_clientconfiguration', 'xAttribute_id')
        
        # Deleting field 'ClientConfiguration.layout'
        db.delete_column('weave_clientconfiguration', 'layout_id')
        
        # Deleting field 'ClientConfiguration.binAttribute'
        db.delete_column('weave_clientconfiguration', 'binAttribute_id')
        
        # Deleting field 'ClientConfiguration.colorAttribute'
        db.delete_column('weave_clientconfiguration', 'colorAttribute_id')
        
        # Deleting field 'ClientConfiguration.mapTitle'
        db.delete_column('weave_clientconfiguration', 'mapTitle')
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Tool'
        db.delete_table('weave_tool')
        
        # Deleting model 'Row'
        db.delete_table('weave_row')
        
        # Adding field 'ClientConfiguration.histogramTitle'
        db.add_column('weave_clientconfiguration', 'histogramTitle', orm['weave.clientconfiguration:histogramTitle'])
        
        # Adding field 'ClientConfiguration.barChartTitle'
        db.add_column('weave_clientconfiguration', 'barChartTitle', orm['weave.clientconfiguration:barChartTitle'])
        
        # Adding field 'ClientConfiguration.yAttribute'
        db.add_column('weave_clientconfiguration', 'yAttribute', orm['weave.clientconfiguration:yAttribute'])
        
        # Adding field 'ClientConfiguration.heightAttribute'
        db.add_column('weave_clientconfiguration', 'heightAttribute', orm['weave.clientconfiguration:heightAttribute'])
        
        # Adding field 'ClientConfiguration.sortingAttribute'
        db.add_column('weave_clientconfiguration', 'sortingAttribute', orm['weave.clientconfiguration:sortingAttribute'])
        
        # Adding field 'ClientConfiguration.xAttribute'
        db.add_column('weave_clientconfiguration', 'xAttribute', orm['weave.clientconfiguration:xAttribute'])
        
        # Adding field 'ClientConfiguration.layout'
        db.add_column('weave_clientconfiguration', 'layout', orm['weave.clientconfiguration:layout'])
        
        # Adding field 'ClientConfiguration.binAttribute'
        db.add_column('weave_clientconfiguration', 'binAttribute', orm['weave.clientconfiguration:binAttribute'])
        
        # Adding field 'ClientConfiguration.colorAttribute'
        db.add_column('weave_clientconfiguration', 'colorAttribute', orm['weave.clientconfiguration:colorAttribute'])
        
        # Adding field 'ClientConfiguration.mapTitle'
        db.add_column('weave_clientconfiguration', 'mapTitle', orm['weave.clientconfiguration:mapTitle'])
        
    
    
    models = {
        'weave.clientconfiguration': {
            'dataTable': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.DataTable']"}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'})
        },
        'weave.row': {
            'config': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rows'", 'to': "orm['weave.ClientConfiguration']"}),
            'height': ('PercentField', [], {'default': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
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
