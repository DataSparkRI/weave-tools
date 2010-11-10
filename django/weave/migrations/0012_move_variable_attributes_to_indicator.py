# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'Indicator.variable_definition'
        db.add_column('weave_indicator', 'variable_definition', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Indicator.year'
        db.add_column('weave_indicator', 'year', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True), keep_default=False)

        # Adding field 'Indicator.category_three'
        db.add_column('weave_indicator', 'category_three', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True), keep_default=False)

        # Adding field 'Indicator.time_group'
        db.add_column('weave_indicator', 'time_group', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Indicator.category_two'
        db.add_column('weave_indicator', 'category_two', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True), keep_default=False)

        # Adding field 'Indicator.category_one'
        db.add_column('weave_indicator', 'category_one', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True), keep_default=False)

        # Adding field 'Indicator.short_label'
        db.add_column('weave_indicator', 'short_label', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Adding field 'Indicator.short_label_prefix'
        db.add_column('weave_indicator', 'short_label_prefix', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Adding field 'Indicator.category_four'
        db.add_column('weave_indicator', 'category_four', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True), keep_default=False)

        # Adding field 'Indicator.name_in_weave'
        db.add_column('weave_indicator', 'name_in_weave', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Adding field 'Indicator.slug'
        db.add_column('weave_indicator', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, null=True, db_index=True), keep_default=False)

        # Adding field 'Indicator.icon'
        db.add_column('weave_indicator', 'icon', self.gf('django.db.models.fields.CharField')(max_length=100, null=True), keep_default=False)

        # Adding field 'Indicator.case_restrictions'
        db.add_column('weave_indicator', 'case_restrictions', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Indicator.dataset_tag'
        db.add_column('weave_indicator', 'dataset_tag', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Adding field 'Indicator.hover_label'
        db.add_column('weave_indicator', 'hover_label', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'Indicator.display'
        db.add_column('weave_indicator', 'display', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True), keep_default=False)

        # Adding field 'Indicator.dataset_name'
        db.add_column('weave_indicator', 'dataset_name', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'Indicator.variable_definition'
        db.delete_column('weave_indicator', 'variable_definition')

        # Deleting field 'Indicator.year'
        db.delete_column('weave_indicator', 'year')

        # Deleting field 'Indicator.category_three'
        db.delete_column('weave_indicator', 'category_three')

        # Deleting field 'Indicator.time_group'
        db.delete_column('weave_indicator', 'time_group')

        # Deleting field 'Indicator.category_two'
        db.delete_column('weave_indicator', 'category_two')

        # Deleting field 'Indicator.category_one'
        db.delete_column('weave_indicator', 'category_one')

        # Deleting field 'Indicator.short_label'
        db.delete_column('weave_indicator', 'short_label')

        # Deleting field 'Indicator.short_label_prefix'
        db.delete_column('weave_indicator', 'short_label_prefix')

        # Deleting field 'Indicator.category_four'
        db.delete_column('weave_indicator', 'category_four')

        # Deleting field 'Indicator.name_in_weave'
        db.delete_column('weave_indicator', 'name_in_weave')

        # Deleting field 'Indicator.slug'
        db.delete_column('weave_indicator', 'slug')

        # Deleting field 'Indicator.icon'
        db.delete_column('weave_indicator', 'icon')

        # Deleting field 'Indicator.case_restrictions'
        db.delete_column('weave_indicator', 'case_restrictions')

        # Deleting field 'Indicator.dataset_tag'
        db.delete_column('weave_indicator', 'dataset_tag')

        # Deleting field 'Indicator.hover_label'
        db.delete_column('weave_indicator', 'hover_label')

        # Deleting field 'Indicator.display'
        db.delete_column('weave_indicator', 'display')

        # Deleting field 'Indicator.dataset_name'
        db.delete_column('weave_indicator', 'dataset_name')
    
    
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
            'keys_query': ('django.db.models.fields.TextField', [], {}),
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
            'dataset_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'dataset_tag': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'hover_label': ('django.db.models.fields.TextField', [], {}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_field_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'key_unit_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.KeyUnitType']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_in_weave': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_label_prefix': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'table_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_group': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'variable_definition': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        'weave.keyunittype': {
            'Meta': {'object_name': 'KeyUnitType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'probing_indicator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'key_unit_types_as_probe'", 'null': 'True', 'to': "orm['weave.Indicator']"})
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
