from django.urls import path
from rest_framework.routers import DefaultRouter

from trials.views import TestModelViewSet
from trials.views import TestTemplateView

router = DefaultRouter()
router.register("items", TestModelViewSet)

urlpatterns = [
    path('<int:test_id>/show/', TestTemplateView)
]

urlpatterns += router.urls
