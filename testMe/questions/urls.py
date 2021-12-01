from rest_framework.routers import DefaultRouter

from questions.views import QuestionModelViewSet

router = DefaultRouter()
router.register("items", QuestionModelViewSet)

urlpatterns = router.urls
