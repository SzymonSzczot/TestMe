from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer


class UserModelView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
