from rest_framework.permissions import BasePermission, SAFE_METHODS


class ISAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        else: return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True    
        return bool(request.user and request.user.is_staff)
        

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user or request.user.is_staff:
            return True
        else: return False


class MembershipBasedPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.is_premium:
            return True
        else: return False