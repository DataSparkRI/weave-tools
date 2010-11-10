# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Tool'
        db.delete_table('weave_tool')

        # Removing M2M table for field table_columns on 'Tool'
        db.delete_table('weave_tool_table_columns')

        # Deleting model 'Layout'
        db.delete_table('weave_layout')

        # Deleting model 'Row'
        db.delete_table('weave_row')

        # Deleting model 'Indicator'
        db.delete_table('weave_indicator')

        # Adding model 'DataTable'
        db.create_table('weave_datatable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('key_unit_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('weave', ['DataTable'])

        # Adding model 'AttributeColumn'
        db.create_table('weave_attributecolumn', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('indicator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicators.Indicator'])),
            ('data_table', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['weave.DataTable'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='indicators', null=True, to=orm['weave.Category'])),
            ('key_unit_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('data_type', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('data_with_keys_query', self.gf('django.db.models.fields.TextField')()),
            ('min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal('weave', ['AttributeColumn'])

        # Deleting field 'ClientConfiguration.data_filter'
        db.delete_column('weave_clientconfiguration', 'data_filter_id')

        # Deleting field 'ClientConfiguration.default_coloring'
        db.delete_column('weave_clientconfiguration', 'default_coloring_id')

        # Deleting field 'ClientConfiguration.years'
        db.delete_column('weave_clientconfiguration', 'years')

        # Adding field 'ClientConfiguration.file'
        db.add_column('weave_clientconfiguration', 'file', self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100, blank=True, null=True), keep_default=False)

        # Deleting field 'KeyUnitType.probing_indicator'
        db.delete_column('weave_keyunittype', 'probing_indicator_id')

        # Deleting field 'KeyUnitType.secondary_probing_indicator'
        db.delete_column('weave_keyunittype', 'secondary_probing_indicator_id')


    def backwards(self, orm):
        
        # Adding model 'Tool'
        db.create_table('weave_tool', (
            ('colorAttribute', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tools_as_color', null=True, to=orm['weave.Indicator'], blank=True)),
            ('histogramTitle', self.gf('django.db.models.fields.CharField')(default='Histogram', max_length=100, null=True, blank=True)),
            ('data_filter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['weave.DataFilter'], null=True, blank=True)),
            ('yAttribute', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tools_as_y', null=True, to=orm['weave.Indicator'], blank=True)),
            ('mapTitle', self.gf('django.db.models.fields.CharField')(default='Rhode Island', max_length=100, null=True, blank=True)),
            ('secondary_geometry_collection', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tools_as_secondary', null=True, to=orm['weave.GeometryCollection'], blank=True)),
            ('height', self.gf('weave.fields.PercentField')()),
            ('width', self.gf('weave.fields.PercentField')()),
            ('xAttribute', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tools_as_x', null=True, to=orm['weave.Indicator'], blank=True)),
            ('barChartTitle', self.gf('django.db.models.fields.CharField')(default='Bar Chart', max_length=100, null=True, blank=True)),
            ('sortingAttribute', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tools_as_sorting', null=True, to=orm['weave.Indicator'], blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('heightAttribute', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tools_as_height', null=True, to=orm['weave.Indicator'], blank=True)),
            ('primary_geometry_collection', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tools_as_primary', null=True, to=orm['weave.GeometryCollection'], blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('binAttribute', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tools_as_bin', null=True, to=orm['weave.Indicator'], blank=True)),
            ('row', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tools', to=orm['weave.Row'])),
        ))
        db.send_create_signal('weave', ['Tool'])

        # Adding M2M table for field table_columns on 'Tool'
        db.create_table('weave_tool_table_columns', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tool', models.ForeignKey(orm['weave.tool'], null=False)),
            ('indicator', models.ForeignKey(orm['weave.indicator'], null=False))
        ))
        db.create_unique('weave_tool_table_columns', ['tool_id', 'indicator_id'])

        # Adding model 'Layout'
        db.create_table('weave_layout', (
            ('config_template', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
        ))
        db.send_create_signal('weave', ['Layout'])

        # Adding model 'Row'
        db.create_table('weave_row', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('width', self.gf('weave.fields.PercentField')()),
            ('height', self.gf('weave.fields.PercentField')()),
            ('config', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rows', to=orm['weave.ClientConfiguration'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('weave', ['Row'])

        # Adding model 'Indicator'
        db.create_table('weave_indicator', (
            ('variable_definition', self.gf('django.db.models.fields.TextField')()),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_three', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='indicators', null=True, to=orm['weave.Category'], blank=True)),
            ('min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('time_group', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('category_two', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('category_one', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('short_label', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('key_unit_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['weave.KeyUnitType'], null=True)),
            ('short_label_prefix', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('category_four', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, db_index=True)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('case_restrictions', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dataset_tag', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hover_label', self.gf('django.db.models.fields.TextField')()),
            ('table_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('key_field_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('display', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('weave', ['Indicator'])

        # Deleting model 'DataTable'
        db.delete_table('weave_datatable')

        # Deleting model 'AttributeColumn'
        db.delete_table('weave_attributecolumn')

        # Adding field 'ClientConfiguration.data_filter'
        db.add_column('weave_clientconfiguration', 'data_filter', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['weave.DataFilter']), keep_default=False)

        # Adding field 'ClientConfiguration.default_coloring'
        db.add_column('weave_clientconfiguration', 'default_coloring', self.gf('django.db.models.fields.related.ForeignKey')(related_name='configs_as_color', null=True, to=orm['weave.Indicator'], blank=True), keep_default=False)

        # Adding field 'ClientConfiguration.years'
        db.add_column('weave_clientconfiguration', 'years', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(max_length=100, null=True, blank=True), keep_default=False)

        # Deleting field 'ClientConfiguration.file'
        db.delete_column('weave_clientconfiguration', 'file')

        # Adding field 'KeyUnitType.probing_indicator'
        db.add_column('weave_keyunittype', 'probing_indicator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='key_unit_types_as_probe', null=True, to=orm['weave.Indicator']), keep_default=False)

        # Adding field 'KeyUnitType.secondary_probing_indicator'
        db.add_column('weave_keyunittype', 'secondary_probing_indicator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='key_unit_types_as_secondary_probe', null=True, to=orm['weave.Indicator'], blank=True), keep_default=False)


    models = {
        'indicators.indicator': {
            'Meta': {'unique_together': "(('name', 'key_unit_type'),)", 'object_name': 'Indicator'},
            'case_restrictions': ('django.db.models.fields.TextField', [], {}),
            'category_four': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'category_one': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'category_three': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'category_two': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'data_type': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'dataset_tag': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hover_label': ('django.db.models.fields.TextField', [], {}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_label': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'short_label_prefix': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'variable_definition': ('django.db.models.fields.TextField', [], {})
        },
        'weave.attributecolumn': {
            'Meta': {'unique_together': "(('name', 'key_unit_type', 'year'),)", 'object_name': 'AttributeColumn'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'indicators'", 'null': 'True', 'to': "orm['weave.Category']"}),
            'data_table': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.DataTable']"}),
            'data_type': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'data_with_keys_query': ('django.db.models.fields.TextField', [], {}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indicators.Indicator']"}),
            'key_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        'weave.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['weave.Category']"})
        },
        'weave.clientconfiguration': {
            'Meta': {'object_name': 'ClientConfiguration'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'weave.datafilter': {
            'Meta': {'object_name': 'DataFilter'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_unit_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.KeyUnitType']", 'null': 'True'}),
            'keys_query': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'weave.datatable': {
            'Meta': {'object_name': 'DataTable'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'weave.geometrycollection': {
            'Meta': {'object_name': 'GeometryCollection'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_unit_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.KeyUnitType']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'weave.keyunittype': {
            'Meta': {'object_name': 'KeyUnitType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['weave']
