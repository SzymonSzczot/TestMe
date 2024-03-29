from rest_framework import viewsets

from questions.models import Question
from questions.serializers import QuestionSerializer


class QuestionModelViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
