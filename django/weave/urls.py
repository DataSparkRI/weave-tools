from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from weave import views
from django.conf import settings

urlpatterns = patterns('',
    url(r'^client_configurations/(?P<config_slug>[\w-]+).xml$', views.client_config, name="weave-client_config"),
)

