from rest_framework.routers import DefaultRouter

from trials.views import TestModelViewSet

router = DefaultRouter()
router.register("items", TestModelViewSet)

urlpatterns = router.urls
