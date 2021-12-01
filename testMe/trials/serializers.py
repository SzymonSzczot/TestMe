from rest_framework import serializers

from questions.serializers import QuestionSerializer
from trials.models import Test


class TestSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True, required=False)

    class Meta:
        model = Test
        fields = (
            "id",
            "name",
            "questions"
        )
