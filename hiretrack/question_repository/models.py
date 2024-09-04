from django.db import models
from Teams.models import Team
from ckeditor.fields import RichTextField

# Create your models here.


class QuestionRepository(models.Model):
    difficulty = [
        ("easy", "easy"),
        ("medium", "medium"),
        ("hard", "hard"),
    ]
    question_text = models.TextField(max_length=500)
    answer_text = RichTextField(null=True, blank=True)
    topic = models.CharField(max_length=100)
    difficulty_level = models.CharField(
        max_length=50, choices=difficulty, default="easy"
    )
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team")

    def __str__(self):
        return f"{self.topic}'s, Questions"