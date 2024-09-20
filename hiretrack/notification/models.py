from django.db import models
from user.models import CustomUser
from interview.models import InterviewForUser


# Create your models here.
class Notification(models.Model):
    TYPE_CHOICE = [("Email", "Email"), ("In_app", "In_app")]
    STATUS_CHOICE = [("Read", "Read"), ("Unread", "Unread")]
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="userid"
    )
    message = models.TextField()
    type = models.CharField(max_length=25, choices=TYPE_CHOICE, default="Email")
    interview_id = models.ForeignKey(
        InterviewForUser, on_delete=models.CASCADE, related_name="interviewid"
    )
    scheduled_at = models.DateTimeField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICE, default="Unread")
    created_at = models.DateTimeField(auto_now_add=True)


class Remainder(models.Model):
    TYPE_CHOICE = [("Email", "Email"), ("In_app", "In_app")]
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user"
    )
    message = models.TextField()
    type = models.CharField(max_length=25, choices=TYPE_CHOICE, default="Email")
    interview_id = models.ForeignKey(
        InterviewForUser, on_delete=models.CASCADE, related_name="interview"
    )
    status = models.BooleanField(default=False, null=True)