from django.core.mail import send_mail
from emailserver.models import UserEmail


class SendNotifications():
    def send(self, notifications: set[str]) -> None:
        for user_id in notifications:
            user_to_notify = UserEmail.objects \
                .filter(id=user_id).first()

            test_message = f"go to http://localhost:8000/view_monitors/{user_id}"

            print(f'sending email to {user_to_notify}')
            send_mail("Test Message", test_message, "ijhaggerty@sep.com",
                      [user_to_notify.email], fail_silently=False)

