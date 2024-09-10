from django.db import models
from user.models import CustomUser
from ckeditor.fields import RichTextField

# Create your models here.


class PreparationModel(models.Model):
    MATERIAL_TYPE_CHOICE = [
        ("Article", "Article"),
        ("Document", "Document"),
        ("Video", "Video"),
    ]

    title = models.CharField(max_length=100)
    content = RichTextField(null=True, blank=True)
    type = models.CharField(
        max_length=25, choices=MATERIAL_TYPE_CHOICE, default="Document"
    )
    link = models.CharField(max_length=225)
    tags = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BookMarkModel(models.Model):
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_id"
    )
    material_id = models.ForeignKey(
        PreparationModel, on_delete=models.CASCADE, related_name="material_id"
    )
    bookmarked_at = models.DateTimeField(auto_now_add=True)
