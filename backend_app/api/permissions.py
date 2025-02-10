from rest_framework.permissions import SAFE_METHODS, BasePermission



class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):       
        return request.user.is_authenticated or request.method in SAFE_METHODS