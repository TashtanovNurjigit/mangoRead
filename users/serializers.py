from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import CustomUser


class CustomUserCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    nickname = serializers.CharField(max_length=30)
    avatar = serializers.ImageField(allow_null=True)

    def validation_username(self, username):
        try:
            User.objects.get(username=username)
            raise ValidationError('User already exists!')
        except User.DoesNotExist:
            return username

    def validation_nickname(self, nickname):
        try:
            User.objects.get(nickname=nickname)
            raise ValidationError('Nickname already exists!')
        except User.DoesNotExist:
            return nickname
