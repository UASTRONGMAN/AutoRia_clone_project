from django.urls import path

from apps.users.views import (
    BecomePremiumUserView,
    CancelAdminUserView,
    CreateAdminUserView,
    UsersBanView,
    UsersCreateView,
    UsersListView,
    UsersUnbanView,
)

urlpatterns = [
    path('/list', UsersListView.as_view(), name='users_list'),
    path('', UsersCreateView.as_view(), name='users_create'),
    path('/<int:pk>/ban', UsersBanView.as_view(), name='users_ban'),
    path('/<int:pk>/unban', UsersUnbanView.as_view(), name='users_unban'),
    path('/<int:pk>/create_admin', CreateAdminUserView.as_view(), name='create_admin_user'),
    path('/<int:pk>/cancel_admin', CancelAdminUserView.as_view(), name='cancel_admin_user'),
    path('/become_premium', BecomePremiumUserView.as_view(), name='become_premium_user'),
]