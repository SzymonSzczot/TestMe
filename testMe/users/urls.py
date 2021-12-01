from rest_framework.routers import DefaultRouter

from users.views import UserModelView

router = DefaultRouter()
router.register("items", UserModelView)

urlpatterns = router.urls
