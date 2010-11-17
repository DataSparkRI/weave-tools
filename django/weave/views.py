from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from weave.models import ClientConfiguration, DataFilter, \
                            KeyUnitType, DataTable
from django.core.urlresolvers import reverse
#from dictionary.models import Variable
from django.conf import settings
from django.contrib.sites.models import Site
from django.views.decorators.cache import cache_page
from django.core.urlresolvers import reverse
from weave import cached_indicator_hierarchy
from webportal.indicators.models import IndicatorData

def index(request):
    "Weave landing page"
    defaults_path = reverse('indicators-default_hierarchy')
    client_config = get_object_or_404(ClientConfiguration,name="Default")
    if not request.GET.has_key('defaults'):
        return HttpResponseRedirect("%s?defaults=%s" % (request.path, reverse('indicators-default_hierarchy')))
    return render_to_response('weave/index.html', { }, 
        context_instance=RequestContext(request))

def client_config(request, config_slug):
    config = get_object_or_404(ClientConfiguration, slug=config_slug)
    return HttpResponse(config.get_xml(), mimetype="application/xml")

def hierarchy(request):
    return render_to_response('weave/main_hierarchy.xml', { 'key_unit_types': KeyUnitType.objects.exclude(name='') }, 
        context_instance=RequestContext(request))

def sqlconfig(request):
    from django.db.models import Q
    context = {
        'key_unit_types': KeyUnitType.objects.all(),
        'weave_settings': settings.WEAVE,
        'data_tables': DataTable.objects.all(),
        'settings': settings,
    }
    return render_to_response('weave/sqlconfig.xml', context, 
        context_instance=RequestContext(request),
        mimetype="application/xml")

