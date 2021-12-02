from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from .managers import UserManager


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(db_index=True, unique=True, max_length=50)
    is_active = models.BooleanField(default=False)

    confirmation_number = models.CharField(max_length=100)
    reset_code = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="avatars/", null=True)

    USERNAME_FIELD = "email"

    class Meta:
        ordering = ("id", )

    objects = UserManager()
    
    def get_details(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }
