import random

from django.apps import apps
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.tokens import default_token_generator

from config import settings
from users import cons
from tools.emails.data import EmailSender
from tools.tools import encode_uid, decode_uid

from .querysets import UserQuerySet


class UserManager(BaseUserManager):

    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def create(self, email, password=None, **kwargs):
        user = self.model(email=email, password=password, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def reset_password(self, user_email):
        User = apps.get_model("users", "User")
        user = User.objects.get(email=user_email["email"])
        credits = self.get_uid_and_activation_token(user)
        self.prepare_code(user, credits["token"], credits["uid"])

    def get_uid_and_activation_token(self, user):
        token_generator = default_token_generator
        token = token_generator.make_token(user)
        uid = encode_uid(user.id)
        return {"uid": uid, "token": token}

    def prepare_code(self, user, token, uid):
        reset_code = int("".join(random.choice("0123456789") for _ in range(6)))
        user.reset_code = reset_code
        user.save()
        self.send_email(user, uid, token, user.reset_code)

    # def create_link(self, uid, token, code):
    #     return f"{settings.CLIENT_DOMAIN}/password/reset/?uid={uid}&token={token}&code={code}"

    def send_email(self, user, uid, token, reset_code):
        EmailSender(self.prepare_data_to_send_email(user, uid, token, reset_code)).send_email()

    def prepare_data_to_send_email(self, user, uid, token, reset_code):
        return {
            "subject": f"{cons.PASSWORD_RESET}",
            "email_to": user.email,
            "user_first_name": user.first_name,
            "user_last_name": user.last_name,
            "uid": uid,
            "token": token,
            "reset_code": reset_code,
            "link": "http://localhost:8000/users/password/reset/confirm"
        }

    def confirm_reset_password(self, **validated_data):
        User = apps.get_model("users", "User")
        user = User.objects.get(id=decode_uid(validated_data["uid"]))
        user.set_password(validated_data["new_password"])
        user.reset_code = None
        user.save(update_fields=["password", "reset_code"])
