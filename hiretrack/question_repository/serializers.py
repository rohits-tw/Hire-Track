from rest_framework import serializers
from question_repository.models import QuestionRepository


class CreateQuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionRepository
        fields = "__all__"


class GetQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionRepository
        fields = "__all__"