from rest_framework import serializers

from questions.models import Question


class QuestionSerializer(serializers.ModelSerializer):

    answers = serializers.SerializerMethodField()

    def get_answers(self, instance: Question):
        return instance.get_answers_secret()

    class Meta:
        model = Question
        fields = (
            "id",
            "name",
            "description",
            "answers",
            "test"
        )
