from django.db import models
from user.models import CustomUser
from ckeditor.fields import RichTextField

# Create your models here.


class InterviewForUser(models.Model):
    INTERVIEW_TYPE = [
        ("Screening Round", "Screening Round"),
        ("Technical 1", "Technical 1"),
        ("Technical 2", "Technical 2"),
        ("HR", "HR")
    ]
    STATUS = [
        ("Scheduled", "Scheduled"),
        ("Completed", "Completed"),
        ("Feedback Pending", "Feedback Pending")
    ]
    user_id = models.CharField(max_length=10, blank=True, null=True)
    interviewer_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="interviewer_id"
    )
    interview_date = models.DateTimeField()
    interview_type = models.CharField(
        max_length=50, choices=INTERVIEW_TYPE, default="Screening Round"
    )
    location = models.CharField(max_length=100, default="Thoughtwin - Old RTO")
    notes = RichTextField(null=True, blank=True)
    status = models.CharField(
        max_length=50, choices=STATUS, default="Scheduled"
    )

    def __str__(self):
        return f"Interview Schedule,{self.interview_type} "