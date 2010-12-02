# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'ClientConfiguration.file'
        db.delete_column('weave_clientconfiguration', 'file')

        # Adding field 'ClientConfiguration.content'
        db.add_column('weave_clientconfiguration', 'content', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'ClientConfiguration.content_format'
        db.add_column('weave_clientconfiguration', 'content_format', self.gf('django.db.models.fields.CharField')(default='json', max_length=4), keep_default=False)

        # Removing unique constraint on 'AttributeColumn', fields ['keyType', 'name', 'year']
        db.delete_unique('weave_attributecolumn', ['keyType', 'name', 'year'])

        # Adding unique constraint on 'AttributeColumn', fields ['keyType', 'name', 'dataTable', 'year']
        db.create_unique('weave_attributecolumn', ['keyType', 'name', 'dataTable', 'year'])


    def backwards(self, orm):
        
        # Adding field 'ClientConfiguration.file'
        db.add_column('weave_clientconfiguration', 'file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True), keep_default=False)

        # Deleting field 'ClientConfiguration.content'
        db.delete_column('weave_clientconfiguration', 'content')

        # Deleting field 'ClientConfiguration.content_format'
        db.delete_column('weave_clientconfiguration', 'content_format')

        # Adding unique constraint on 'AttributeColumn', fields ['keyType', 'name', 'year']
        db.create_unique('weave_attributecolumn', ['keyType', 'name', 'year'])

        # Removing unique constraint on 'AttributeColumn', fields ['keyType', 'name', 'dataTable', 'year']
        db.delete_unique('weave_attributecolumn', ['keyType', 'name', 'dataTable', 'year'])


    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'weave.attributecolumn': {
            'Meta': {'unique_together': "(('name', 'keyType', 'year', 'dataTable'),)", 'object_name': 'AttributeColumn'},
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
            'content': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'content_format': ('django.db.models.fields.CharField', [], {'default': "'json'", 'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
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
