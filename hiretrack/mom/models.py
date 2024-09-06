from django.db import models
from interview.models import InterviewForUser
from user.models import CustomUser
from ckeditor.fields import RichTextField


class Mom(models.Model):
    interview_id = models.ForeignKey(
        InterviewForUser, on_delete=models.CASCADE, related_name="interview_id"
    )
    author_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="author_id"
    )
    notes = RichTextField(null=True, blank=True)
    action_items = RichTextField(null=True, blank=True)
    next_step = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Minute of meeting {self.interview_id}"
