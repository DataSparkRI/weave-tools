from django.contrib import admin
from django.conf import settings
from weave.models import ClientConfiguration, GeometryCollection, \
                            AttributeColumn

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
admin.site.register(AttributeColumn)
admin.site.register(GeometryCollection)
