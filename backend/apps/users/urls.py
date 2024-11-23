from django.urls import path

from apps.users.views import UsersCreateView, UsersListView

urlpatterns = [
    path('', UsersListView.as_view(), name='users_list'),
    path('/create', UsersCreateView.as_view(), name='users_create'),
]