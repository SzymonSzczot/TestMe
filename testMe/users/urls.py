from rest_framework.routers import DefaultRouter

from users.views import UserModelViewSet

router = DefaultRouter()
router.register("items", UserModelViewSet)

urlpatterns = router.urls
