from rest_framework import serializers
from preparation.models import PreparationModel, BookMarkModel


class AddPreparationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreparationModel
        fields = ["title", "content", "type", "link", "tags"]


class GetAllMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreparationModel
        fields = ["id", "title", "content", "type", "link", "tags", "created_at"]


class AddBookMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMarkModel
        fields = ["user_id", "material_id"]


class GetBookMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreparationModel
        fields = ["id", "title", "content", "type", "link", "tags"]


class GetBookMarkByUserIdSerializer(serializers.ModelSerializer):
    material = GetBookMarkSerializer(read_only=True)

    class Meta:
        model = BookMarkModel
        fields = ["id", "material", "bookmarked_at", "user_id"]
