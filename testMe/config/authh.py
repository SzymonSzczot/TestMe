from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from users.models import User


class SettingsBackend(BaseBackend):

    def authenticate(self, request, email=None, password=None):
        user = User.objects.get(email=email)
        if check_password(password, user.password):
            user_final = user
        else:
            user_final = ({"message": "bad"})
        return user_final

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None