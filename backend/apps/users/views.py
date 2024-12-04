from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from apps.users.serializers import UserSerializer

UserModel = get_user_model()


class UsersCreateView(CreateAPIView):

    """
    Реєстрація користувача.
    """

    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
    pagination_class = None

class UsersListView(ListAPIView):

    """
    Вивід всіх зареєстрованих користувачів.
    """

    queryset = UserModel.objects.select_related('profile').all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )
    pagination_class = None

class UsersBanView(GenericAPIView):

    """
    Бан користувача.
    """

    queryset = UserModel.objects.select_related('profile').all()
    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data ,status=status.HTTP_200_OK)

class UsersUnbanView(GenericAPIView):
    """
    Розбан користувача.
    """

    queryset = UserModel.objects.select_related('profile').all()
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data ,status=status.HTTP_200_OK)


class CreateAdminUserView(GenericAPIView):

    """
    Надання прав адміністратора.
    """

    queryset = UserModel.objects.select_related('profile').all()
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CancelAdminUserView(GenericAPIView):

    """
    Відміна прав адміністратора.
    """

    queryset = UserModel.objects.select_related('profile').all()
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BecomePremiumUserView(GenericAPIView):

    """
    Набування авторизованим користувачем преміум статусу.
    """

    permission_classes = (IsAuthenticated, )

    def patch(self, *args, **kwargs):
        user = self.request.user
        user.is_premium_user = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

