from emailserver.models import TourDate, MonitorWindow

class ComputeNotifications():
    def get_changed_tours(self):
        
        return TourDate.objects.filter(notification_sent=False)
    
    def compute_notifications(self):
        changed_tours = self.get_changed_tours()

        notification_sent = False

        for tour in changed_tours:
            relevant_monitors = MonitorWindow.objects.filter(tour=tour).complex_filter

            for monitor in relevant_monitors:
                if tour.date > monitor.start_date and tour.date < monitor.end_date:
                    # send notifications
                    notification_sent = True

        return notification_sent


