
from south.db import db
from django.db import models
from webportal.weave.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'ClientConfiguration'
        db.create_table('weave_clientconfiguration', (
            ('yAttribute', orm['weave.ClientConfiguration:yAttribute']),
            ('histogramTitle', orm['weave.ClientConfiguration:histogramTitle']),
            ('layout', orm['weave.ClientConfiguration:layout']),
            ('name', orm['weave.ClientConfiguration:name']),
            ('colorAttribute', orm['weave.ClientConfiguration:colorAttribute']),
            ('mapTitle', orm['weave.ClientConfiguration:mapTitle']),
            ('binAttribute', orm['weave.ClientConfiguration:binAttribute']),
            ('id', orm['weave.ClientConfiguration:id']),
            ('xAttribute', orm['weave.ClientConfiguration:xAttribute']),
            ('heightAttribute', orm['weave.ClientConfiguration:heightAttribute']),
            ('barChartTitle', orm['weave.ClientConfiguration:barChartTitle']),
            ('dataTable', orm['weave.ClientConfiguration:dataTable']),
            ('sortingAttribute', orm['weave.ClientConfiguration:sortingAttribute']),
            ('slug', orm['weave.ClientConfiguration:slug']),
        ))
        db.send_create_signal('weave', ['ClientConfiguration'])
        
        # Adding model 'DataTable'
        db.create_table('weave_datatable', (
            ('description', orm['weave.DataTable:description']),
            ('keys_query', orm['weave.DataTable:keys_query']),
            ('id', orm['weave.DataTable:id']),
            ('name', orm['weave.DataTable:name']),
        ))
        db.send_create_signal('weave', ['DataTable'])
        
        # Adding model 'Indicator'
        db.create_table('weave_indicator', (
            ('key_field_name', orm['weave.Indicator:key_field_name']),
            ('table_name', orm['weave.Indicator:table_name']),
            ('id', orm['weave.Indicator:id']),
            ('name', orm['weave.Indicator:name']),
        ))
        db.send_create_signal('weave', ['Indicator'])
        
        # Adding model 'Layout'
        db.create_table('weave_layout', (
            ('config_template', orm['weave.Layout:config_template']),
            ('id', orm['weave.Layout:id']),
            ('name', orm['weave.Layout:name']),
        ))
        db.send_create_signal('weave', ['Layout'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'ClientConfiguration'
        db.delete_table('weave_clientconfiguration')
        
        # Deleting model 'DataTable'
        db.delete_table('weave_datatable')
        
        # Deleting model 'Indicator'
        db.delete_table('weave_indicator')
        
        # Deleting model 'Layout'
        db.delete_table('weave_layout')
        
    
    
    models = {
        'weave.clientconfiguration': {
            'barChartTitle': ('django.db.models.fields.CharField', [], {'default': "'Bar Chart'", 'max_length': '100'}),
            'binAttribute': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'config_as_bin'", 'to': "orm['weave.Indicator']"}),
            'colorAttribute': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'config_as_color'", 'to': "orm['weave.Indicator']"}),
            'dataTable': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.DataTable']"}),
            'heightAttribute': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'config_as_height'", 'to': "orm['weave.Indicator']"}),
            'histogramTitle': ('django.db.models.fields.CharField', [], {'default': "'Histogram'", 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layout': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.Layout']"}),
            'mapTitle': ('django.db.models.fields.CharField', [], {'default': "'Rhode Island'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'sortingAttribute': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'config_as_sorting'", 'to': "orm['weave.Indicator']"}),
            'xAttribute': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'config_as_x'", 'to': "orm['weave.Indicator']"}),
            'yAttribute': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'config_as_y'", 'to': "orm['weave.Indicator']"})
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
        }
    }
    
    complete_apps = ['weave']
