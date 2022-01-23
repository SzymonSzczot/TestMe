from rest_framework.routers import DefaultRouter
from django.urls import path

from categories.views import CategoryModelViewSet, category

router = DefaultRouter(trailing_slash=False)
router.register("items", CategoryModelViewSet)

urlpatterns = [
    path('<category_name>', category),
]

urlpatterns += router.urls
