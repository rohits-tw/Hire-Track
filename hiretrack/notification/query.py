from notification.models import Notification, Remainder


def get_notification_details_by_id(id):
    notifications = Notification.objects.get(id=id)
    return notifications


def get_by_remainder_id(id):
    remainder = Remainder.objects.get(id=id)
    return remainder
