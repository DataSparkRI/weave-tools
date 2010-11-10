import os
import shutil

from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.files.storage import FileSystemStorage
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


from weave.fields import PercentField
from indicators.models import Indicator
#from dictionary.models import Variable

class Category(models.Model):
    parent = models.ForeignKey('self',null=True,blank=True,related_name='children')
    name = models.CharField(max_length=300)

    def __unicode__(self):
        return u'%s' % (self.name)

class KeyUnitType(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def get_data_table(self):
        return DataTable.objects.get(name=self.name)
    
    def __unicode__(self):
        return u'%s' % (self.name)

class DataTableManager(models.Manager):
    def get_or_create_for_filter(self, data_filter):
        return self.get_or_create(
            name="%s - %s" % (data_filter.key_unit_type, data_filter.name),
            key_unit_type = data_filter.key_unit_type
        )

class DataTable(models.Model):
    name = models.CharField(max_length=100)
    key_unit_type = models.CharField(max_length=100)
    
    objects = DataTableManager()
    
    def ordered_attribute_columns(self):
        return self.attributecolumn_set.order_by('display_name', 'year')

class AttributeColumnManager(models.Manager):
    def years(self):
        return self.exclude(year=None).exclude(year='') \
                   .values_list('year', flat=True).order_by('year').distinct()
 
class AttributeColumn(models.Model):
    DATA_TYPE_CHOICES = (
        ('number', 'number'),
        ('text', 'text')
    )
    # TODO: Not sure this relation should be here -- now weave depends on the indicators app
    # Ideally remove this, and let Indicator find its AttributeColumns, not the other way around.
    # maybe a GenericForeignKey?

    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    source = generic.GenericForeignKey('content_type', 'object_id')
    
    #indicator = models.ForeignKey(Indicator,null=True,blank=True)
    data_table = models.ForeignKey(DataTable)
    name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=255)
    category = models.ForeignKey('Category',null=True,blank=True,related_name='indicators')
    key_unit_type = models.CharField(max_length=100)
    data_type = models.CharField(max_length=6,choices=DATA_TYPE_CHOICES)
    
    data_with_keys_query = models.TextField()
    
    min = models.IntegerField(null=True,blank=True)
    max = models.IntegerField(null=True,blank=True)

    # can hold values other than years
    year = models.CharField(max_length=50,null=True,blank=True)
    
    objects = AttributeColumnManager()

    @models.permalink
    def get_absolute_url(self):
        return ('dictionary-indicator', (), {'indicator_slug': self.slug})
    
    @property
    def weave_display_name(self):
        return self.display_name

    @property
    def full_display_name(self):
        return self.display_name

    def __unicode__(self):
        return u"%s" % self.full_display_name

    class Meta:
        unique_together = (
            ('name', 'key_unit_type', 'year', ),
        )    
    
class DataFilter(models.Model):
    file = models.FileField(upload_to='data_filter_files',blank=True)
    name = models.CharField(max_length=100,unique=True)
    display = models.BooleanField(default=True)
    key_unit_type = models.ForeignKey(KeyUnitType,null=True)
    
    def get_xml(self):
        from django.template.loader import render_to_string
        context = { 'data_filter': self, 'indicators': Indicator.objects.all() }
        return render_to_string('weave/data_filter_config.xml', context)
    
    def indicator_name(self, indicator):
        "Returns the displayed name of an indicator when used in this data filter"
        return "%s (%s)" % (indicator.weave_display_name, self.name)

    def get_data_table(self):
        try:
            return DataTable.objects.get(name='%s - %s' % (self.key_unit_type.name, self.name))
        except DataTable.DoesNotExist:
            return None
    
    def save(self, *args, **kwargs):
        super(DataFilter, self).save(*args, **kwargs)

        try:
            # update DataFilterKey values based on the current file
            # file.file.file is really unfortunate, please fix when I have more time
            keys = map(lambda k: k.strip().split(',')[0],
                self.file.file.file.readlines())
            self.datafilterkey_set.all().delete()
            for key in keys:
                self.datafilterkey_set.create(key_value=key)
        except IOError:
            # file missing is recorable, just leave the DataFilter as is
            pass
    
    def modify_query(self, query):
        """ Take a data with keys query and append a sql clause to return
        only data that matches the current filter.
        """
        filter_sql = "AND key_value in (SELECT key_value from weave_datafilterkey WHERE data_filter_id = %s)" % self.pk
        if query.endswith(' '):
            return "".join([query, filter_sql])
        else:
            return " ".join([query, filter_sql])
        
    def __unicode__(self):
         return "%s" % self.name

class DataFilterKey(models.Model):
    data_filter = models.ForeignKey(DataFilter)
    key_value = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s - %s" % (self.data_filter, self.key_value)

# stores files in Glassfish's docroot, rather than MEDIA_ROOT
# a Proxy matching the base_url should be setup in Apache
weave_config_storage = FileSystemStorage(location=settings.WEAVE['DOCROOT'], base_url="/weave_docroot/")
class ClientConfiguration(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True,db_index=True)
    file = models.FileField(upload_to='weave_config',blank=True, storage=weave_config_storage, null=True)
    
    def save(self, *args, **kwargs):
        from webportal.unique_slugify import unique_slugify
        unique_slugify(self, self.name)
        
        # create a default weave configuration file if one doesn't exist
        #if self.file.name == '':
        #    upload_path = os.path.join('%s.xml' % self.slug)
        #    default_weave_path = os.path.join(
        #            settings.WEAVE['DOCROOT'],'default.xml')
        #    target_path = os.path.join(
        #            settings.WEAVE['DOCROOT'], upload_path)
        #    shutil.copyfile(default_weave_path, target_path)
        #    self.file = upload_path
        super(ClientConfiguration, self).save(*args, **kwargs)
        
    def get_defaults_path(self):
        return '/weave_docroot/%s.xml' % self.slug
        if not self.file:
            return '/weave_docroot/default.xml'
        return self.file.url
    
    def __unicode__(self):
        return "%s" % self.name

class GeometryCollection(models.Model):
    """A geometry collection that's been imported through the Weave Admin
    console.
    """
    name = models.CharField(max_length=100,null=False,blank=False)
    key_unit_type = models.ForeignKey(KeyUnitType,null=True)
    
    def __unicode__(self):
        return u'Geometry Collection: %s' % (self.name, )

