from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.conf import settings

from weave.models import ClientConfiguration 

def client_config(request, config_slug):
    config = get_object_or_404(ClientConfiguration, slug=config_slug)
    return HttpResponse(config.get_xml(), mimetype="application/xml")

