from django.core.management.base import BaseCommand
from emailserver.helpers.fetchtourdateshelper import FetchTourDates
import datetime

class Command(BaseCommand):
    help = "Fetches all tour dates as defined by the NPS"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        FetchTourDates(stdout=self.stdout).get_tour_dates()
