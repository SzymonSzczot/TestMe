from rest_framework import status
from rest_framework.response import Response
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_text, force_bytes
from rest_framework.exceptions import APIException
from . import cons


def encode_uid(pk):
    return force_text(urlsafe_base64_encode(force_bytes(pk)))


def decode_uid(pk):
    return force_text(urlsafe_base64_decode(pk))

class EmailException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = cons.EMAIL_COULD_NOT_BE_SENT

    def __init__(self):
        self.detail = {"detail": force_text(self.default_detail)}


class PasswordResetShortcut:

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response({"detail": cons.EMAIL_HAS_BEEN_SENT}, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmShortcut:

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response({"detail": cons.PASSWORD_HAS_BEEN_CHANGED}, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

