from django.apps import apps
from django.contrib.auth.base_user import BaseUserManager
from .querysets import UserQuerySet

class UserManager(BaseUserManager):

    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)