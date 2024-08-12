from django.db import models
from user.models import BaseModel
from django.conf import settings


class Team(BaseModel):

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    team_lead = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='team_lead')

    def __str__(self):
        return self.name
