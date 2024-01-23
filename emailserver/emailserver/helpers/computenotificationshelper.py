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

        notification_sent = False
        activated_emails = set()
        
        for tour_date in changed_tour_dates:
            relevant_monitors = MonitorWindow.objects.filter(tour=tour_date.tour)

            for monitor in relevant_monitors:
                if tour_date.date > monitor.start_date and tour_date.date < monitor.end_date:
                    activated_emails.add(monitor.email)
                    notification_sent = True

        return notification_sent


