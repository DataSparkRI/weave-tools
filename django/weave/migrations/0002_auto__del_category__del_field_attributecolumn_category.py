# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('weave_category')

        # Deleting field 'AttributeColumn.category'
        db.delete_column('weave_attributecolumn', 'category_id')


    def backwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('weave_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='children', null=True, to=orm['weave.Category'], blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('weave', ['Category'])

        # Adding field 'AttributeColumn.category'
        db.add_column('weave_attributecolumn', 'category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='indicators', null=True, to=orm['weave.Category'], blank=True), keep_default=False)


    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'weave.attributecolumn': {
            'Meta': {'unique_together': "(('name', 'keyType', 'year'),)", 'object_name': 'AttributeColumn'},
            'connection': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'dataTable': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'dataType': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'geometryCollection': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyType': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'max': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'min': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'sqlQuery': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'weave.clientconfiguration': {
            'Meta': {'object_name': 'ClientConfiguration'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'weave.datafilter': {
            'Meta': {'object_name': 'DataFilter'},
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_unit_type': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'weave.datafilterkey': {
            'Meta': {'object_name': 'DataFilterKey'},
            'data_filter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['weave.DataFilter']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_value': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'weave.geometrycollection': {
            'Meta': {'object_name': 'GeometryCollection'},
            'connection': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importNotes': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'keyType': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'schema': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'tablePrefix': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['weave']
