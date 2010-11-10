from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
import sys

class Command(BaseCommand):
    option_list = BaseCommand.option_list# + (
    help = ''
    args = ''

    def handle(self, *args, **options):
        from weave.load import run
        run()
