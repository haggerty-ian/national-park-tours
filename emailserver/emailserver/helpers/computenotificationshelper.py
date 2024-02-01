from emailserver.models import TourDate, MonitorWindow
from io import StringIO


class ComputeNotifications():
    stdout: StringIO

    def __init__(self, stdout: StringIO) -> None:
        self.stdout = stdout

    def get_changed_tour_dates(self):
        return TourDate.objects.filter(notification_sent=False)

    def compute_notifications(self):
        changed_tour_dates = self.get_changed_tour_dates()
        activated_emails = set()

        for tour_date in changed_tour_dates:
            relevant_monitors = MonitorWindow.objects \
                .filter(tour=tour_date.tour)

            for monitor in relevant_monitors:
                if (tour_date.date >= monitor.start_date
                   or monitor.start_date is None) and \
                   (tour_date.date <= monitor.end_date
                   or monitor.end_date is None):
                    self.stdout.write(f"""monitor {monitor} activated
                                       with email {monitor.email.id}""")
                    activated_emails.add(monitor.email.id)

        return activated_emails
