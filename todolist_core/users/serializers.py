from rest_framework import serializers
from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ('email', 'password')
