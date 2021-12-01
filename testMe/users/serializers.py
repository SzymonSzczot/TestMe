from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "password"
        )
