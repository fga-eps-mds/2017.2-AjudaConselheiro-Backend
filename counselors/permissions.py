from rest_framework import permissions

class IsCounselorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
        if (request.user):
            return account == request.user
        return False