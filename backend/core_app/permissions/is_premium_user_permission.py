from rest_framework.permissions import BasePermission


class IsPremiumUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_active and request.user.is_premium_user)