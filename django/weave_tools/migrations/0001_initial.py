# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AttributeColumn'
        db.create_table('weave_tools_attributecolumn', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('keyType', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('dataType', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('dataTable', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('geometryCollection', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('min', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('max', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('connection', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('sqlQuery', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('weave_tools', ['AttributeColumn'])

        # Adding unique constraint on 'AttributeColumn', fields ['name', 'keyType', 'year', 'dataTable']
        db.create_unique('weave_tools_attributecolumn', ['name', 'keyType', 'year', 'dataTable'])

        # Adding model 'GeometryCollection'
        db.create_table('weave_tools_geometrycollection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('keyType', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('importNotes', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('connection', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('schema', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('tablePrefix', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('weave_tools', ['GeometryCollection'])

        # Adding model 'ClientConfiguration'
        db.create_table('weave_tools_clientconfiguration', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('content', self.gf('django.db.models.fields.TextField')(default='')),
            ('content_format', self.gf('django.db.models.fields.CharField')(default='json', max_length=4)),
        ))
        db.send_create_signal('weave_tools', ['ClientConfiguration'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'AttributeColumn', fields ['name', 'keyType', 'year', 'dataTable']
        db.delete_unique('weave_tools_attributecolumn', ['name', 'keyType', 'year', 'dataTable'])

        # Deleting model 'AttributeColumn'
        db.delete_table('weave_tools_attributecolumn')

        # Deleting model 'GeometryCollection'
        db.delete_table('weave_tools_geometrycollection')

        # Deleting model 'ClientConfiguration'
        db.delete_table('weave_tools_clientconfiguration')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'weave_tools.attributecolumn': {
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
        'weave_tools.clientconfiguration': {
            'Meta': {'object_name': 'ClientConfiguration'},
            'content': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'content_format': ('django.db.models.fields.CharField', [], {'default': "'json'", 'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'weave_tools.geometrycollection': {
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

    complete_apps = ['weave_tools']
