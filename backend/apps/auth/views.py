from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core_app.dataclasses.user_dataclass import User
from core_app.services.email_service import EmailService
from core_app.services.jwt_service import JWTService, RecoveryPasswordToken, UserActivationToken

from apps.auth.serializers import EmailSerializer, PasswordSerializer
from apps.users.serializers import UserSerializer

UserModel: User = get_user_model()

class UserActivationView(GenericAPIView):

    """
    Активація користувача через пошту.
    """

    permission_classes = (AllowAny,)

    def patch(self, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.verify_token(token, UserActivationToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecoveryPasswordRequestView(GenericAPIView):
    """
    Запит на відновлення пароля через пошту.
    """

    permission_classes = (AllowAny,)
    serializer_class = EmailSerializer

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = EmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, **serializer.data)
        EmailService.recovery_password(user)
        return Response(status=status.HTTP_200_OK)

class RecoveryPasswordView(GenericAPIView):
    """
    Створення нового паролю.
    """

    permission_classes = (AllowAny,)
    serializer_class = PasswordSerializer

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = PasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        token = kwargs['token']
        user = JWTService.verify_token(token, RecoveryPasswordToken)
        user.set_password(serializer.data['password'])
        user.save()
        return Response({"detail": "Your password has been changed."}, status=status.HTTP_200_OK)