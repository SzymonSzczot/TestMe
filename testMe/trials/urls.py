from django.urls import path
from rest_framework.routers import DefaultRouter

from trials.views import TestModelViewSet
from trials.views import TestTemplateView
from trials.views import TestValidateAPIView

router = DefaultRouter()
router.register("items", TestModelViewSet)

urlpatterns = [
    path('<int:test_id>/show/', TestTemplateView.as_view()),
    path('<int:test_id>/mark/', TestValidateAPIView.as_view())
]

urlpatterns += router.urls
