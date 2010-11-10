from django.contrib import admin
from django.conf import settings
from weave.models import (ClientConfiguration, DataFilter,
                          KeyUnitType, Category, GeometryCollection, 
                          DataFilter, DataFilterKey)

class ClientConfigurationAdmin(admin.ModelAdmin):
    exclude = ('file', )
    prepopulated_fields = {"slug": ("name",)}
    def change_view(self, request, object_id, extra_context=None):
        context = {
            'weave_settings': settings.WEAVE
        }
        return super(ClientConfigurationAdmin, self).change_view(request,
            object_id, extra_context=context)
    
admin.site.register(ClientConfiguration, ClientConfigurationAdmin)


class DataFilterAdmin(admin.ModelAdmin):
    list_display = ('name','key_unit_type',)
    list_editable = ('key_unit_type',)
admin.site.register(DataFilter, DataFilterAdmin)

admin.site.register(KeyUnitType)
admin.site.register(Category)


admin.site.register(GeometryCollection)
admin.site.register(DataFilterKey)
