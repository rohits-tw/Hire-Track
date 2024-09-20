from django.contrib import admin
from notification.models import Notification, Remainder

# Register your models here.
admin.site.register(Notification)

admin.site.register(Remainder)
