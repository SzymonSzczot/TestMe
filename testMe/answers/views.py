from rest_framework import viewsets

from answers.models import Answer
from answers.serializers import AnswerSerializer


class AnswerModelViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
