from rest_framework import viewsets

from trials.models import Test
from trials.serializers import TestSerializer


class TestModelViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
