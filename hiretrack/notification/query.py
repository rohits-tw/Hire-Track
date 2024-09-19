from notification.models import Notification


def get_notification_details_by_id(id):
    notifications = Notification.objects.get(id=id)
    return notifications