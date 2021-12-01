from django.views.generic import TemplateView
from rest_framework import viewsets

from trials.models import Test
from trials.serializers import TestSerializer


class TestModelViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestTemplateView(TemplateView):

    permission_classes = []
    template_name = f"generic_test.html"

    def get_queryset(self):
        return Test.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["test"] = self.get_queryset().first
        return context
