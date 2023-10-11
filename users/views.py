from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import CustomUser
from .serializers import CustomUserCreateSerializer


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = CustomUserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = CustomUser.create_user_profile(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            nickname=serializer.validated_data['nickname'],
            avatar=serializer.validated_data['avatar'],
        )
        return Response(data={'user_id': user.id})


class AuthorizationAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token_, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token_.key})

        return Response(status=status.HTTP_401_UNAUTHORIZED)

