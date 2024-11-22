from django.urls import path

from apps.users.views import UsersListCreateView

urlpatterns = [
    path('', UsersListCreateView.as_view(), name='users_list_create'),
]