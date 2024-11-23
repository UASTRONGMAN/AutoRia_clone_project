from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser

from apps.users.serializers import UserSerializer

UserModel = get_user_model()


class UsersCreateView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
    pagination_class = None

class UsersListView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )
    pagination_class = None