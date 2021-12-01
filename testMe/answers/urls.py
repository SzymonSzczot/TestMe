from rest_framework.routers import DefaultRouter

from answers.views import AnswerModelViewSet

router = DefaultRouter()
router.register("items", AnswerModelViewSet)

urlpatterns = router.urls
