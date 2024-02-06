from django.core.management.base import BaseCommand
from emailserver.helpers.computenotificationshelper import ComputeNotifications
from emailserver.helpers.sendnotificationshelper import SendNotifications
from emailserver.models import TourDate, Facility, Tour
from datetime import date


class Command(BaseCommand):
    help = "Fetches all facilities as defined by the NPS"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        test_tour = Tour.objects.filter(id=127).first()
        test_facility = Facility.objects.filter(id=52).first()

        test_tour_date = TourDate(date=date.today(), tour=test_tour, facility=test_facility)
        test_tour_date.save()

        notifications = ComputeNotifications(stdout=self.stdout)\
            .compute_notifications()

        SendNotifications().send(notifications)
