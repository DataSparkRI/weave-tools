from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from weave import views
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', views.index, name="weave-index"),
    url(r'^client_configurations/(?P<config_slug>[\w-]+).xml$', views.client_config, name="weave-client_config"),
    url(r'^sqlconfig.xml', views.sqlconfig, name='weave-sqlconfig'),
    url(r'^hierarchy.xml', views.hierarchy, name='weave-hierarchy'),
    url(r'^services.xml', direct_to_template, {
        'template': 'services.xml',
        'mimetype': 'application/xml',
        'extra_context': {'services_host': settings.WEAVE['SERVICES_HOST']}
    }),
    url(r'^weaveStyle.css', direct_to_template, {'template': 'weaveStyle.css','mimetype': 'text/css'}),
)

