from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.users.serializers import UserSerializer

UserModel = get_user_model()


class UsersListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
    pagination_class = None