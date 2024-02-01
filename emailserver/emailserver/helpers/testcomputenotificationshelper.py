from django.test import TestCase
from emailserver.helpers.computenotificationshelper import ComputeNotifications
from emailserver.models import TourDate, Tour, Facility, MonitorWindow, UserEmail
from datetime import date, timedelta
from io import StringIO

class ComputeNotificationsTestCase(TestCase):
    command = ComputeNotifications(StringIO())

    def setUp(self):
        self.test_facility = Facility(name="testFacility", external_reference_id=1234)
        self.test_facility.save()
        self.test_tour = Tour(name="testTour", external_reference_id=2345, facility=self.test_facility)
        self.test_tour.save()
        self.test_email = UserEmail(email="testuser@gmail.com")
        self.test_email.save()

    def test_tour_date_default_false(self):
        test_tour_date = TourDate(date=date.today(), tour=self.test_tour)

        self.assertFalse(test_tour_date.notification_sent)

    def test_notifications_computed(self):
        test_tour_date = TourDate(date=date.today(), tour=self.test_tour, facility=self.test_facility)
        test_tour_date.save()

        test_monitor_window = MonitorWindow(start_date=date.today() - timedelta(days=1), end_date=date.today() + timedelta(days=1), tour=self.test_tour, email=self.test_email)
        test_monitor_window.save()

        second_test_monitor_window = MonitorWindow(start_date=date.today() - timedelta(days=2), end_date=date.today() - timedelta(days=1), tour=self.test_tour, email=self.test_email)
        second_test_monitor_window.save()

        second_test_monitor_window = MonitorWindow(start_date=date.today() - timedelta(days=1), end_date=date.today() + timedelta(days=1), tour=self.test_tour, email=self.test_email)
        second_test_monitor_window.save()

        self.assertTrue(self.command.compute_notifications())
