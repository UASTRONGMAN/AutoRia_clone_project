from rest_framework.permissions import BasePermission


class IsCarDealership(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_active and request.user.is_premium_user and request.user.is_staff)