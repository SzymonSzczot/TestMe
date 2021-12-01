from django.views.generic import TemplateView
from rest_framework import views
from rest_framework import viewsets
from rest_framework.response import Response

from config.settings import BASE_DIR
from trials.models import Test
from trials.serializers import TestSerializer


class TestModelViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestTemplateView(TemplateView):

    permission_classes = []
    template_name = BASE_DIR + f"/templates/generic_test.html"

    def get_queryset(self):
        return Test.objects.all()

    def get_context_data(self, test_id, **kwargs):
        context = super().get_context_data(**kwargs)
        context["test"] = self.get_queryset().filter(id=test_id).prefetch_related("questions__answers").first()
        return context


class TestValidateAPIView(views.APIView):
    PASSED = "passed"
    FAILED = "failed"
    UNKNOWN = "unknown"

    PASSED = {
        True: PASSED,
        False: FAILED
    }

    def get_score(self, test: Test, answers):
        return test.get_score(answers)

    def post(self, request, test_id, **kwargs):
        test = Test.objects.get(id=test_id)
        score = self.get_score(test, request.data["answers"])
        status = score >= test.passing_score
        return Response({
            "status": self.PASSED.get(status, self.UNKNOWN),
            "points": score
        })
