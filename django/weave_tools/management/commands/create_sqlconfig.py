import os

from django.core.management.base import BaseCommand, CommandError
from django.template.loader import render_to_string
from django.conf import settings

from weave.models import AttributeColumn, GeometryCollection

class Command(BaseCommand):
    help = "Create a default sqlconfig.xml for Weave"

    requires_model_validation = False

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError("need exactly argument for the target path")

        path, = args

        if os.path.exists(path):
            raise CommandError("file already exists")

        print "Creating '%s'..." % path
        context = {
            'attribute_column_table': AttributeColumn._meta.db_table,
            'geometry_column_table': GeometryCollection._meta.db_table,
            'weave_settings': settings.WEAVE if hasattr(settings, 'WEAVE') else {},
            'settings': settings
        }
        content = render_to_string('weave/sqlconfig.xml', context)
        open(path, 'w').write(content)


