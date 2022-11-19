from rest_framework.serializers import ModelSerializer
from workers_auth.models import LannisterUser, Role


class UserSerializer(ModelSerializer):
    class Meta:
        ordering = ["id"]
        model = LannisterUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "roles",
        )


class RoleSerializer(ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Role
        fields = ["id", "users"]
