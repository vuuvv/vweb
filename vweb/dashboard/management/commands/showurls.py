from django.core.management.base import BaseCommand, CommandError
from vweb.utils.urls import get_urls

class Command(BaseCommand):
    help = "show all url patterns"

    def handle(self, *args, **options):
        for pattern, view in get_urls():
            self.stdout.write("%s: %s\n" % (pattern, view))

