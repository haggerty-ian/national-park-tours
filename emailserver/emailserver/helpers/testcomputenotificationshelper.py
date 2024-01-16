from django.test import TestCase
from emailserver.helpers.computenotificationshelper import ComputeNotifications
from emailserver.models import TourDate, Tour, Facility, MonitorWindow
from datetime import date, timedelta

class ComputeNotificationsTestCase(TestCase):
    command = ComputeNotifications()

    def setUp(self):
        self.test_facility = Facility(name="testFacility", external_reference_id=1234)
        self.test_tour = Tour(name="testTour", external_reference_id=2345, facility=self.test_facility)

    def test_tour_date_default_false(self):
        test_tour_date = TourDate(date=date.today(), tour=self.test_tour)

        self.assertFalse(test_tour_date.notification_sent)

    def test_notifications_computed(self):
        test_tour_date = TourDate(date=date.today(), tour=self.test_tour)


        print(date.today() - timedelta(days=1))
        print(date.today())

        test_monitor_window = MonitorWindow(start_date=date.today() - timedelta(days=1), end_date=date.today() + timedelta(days=1), tour=self.test_tour)

        self.assertTrue(self.command.compute_notifications())
