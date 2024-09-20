from notification.models import Notification, Remainder


def get_by_id(id):
    notification = Notification.objects.get(id=id)
    return notification


def get_by_remainder_id(id):
    remainder = Remainder.objects.get(id=id)
    return remainder
