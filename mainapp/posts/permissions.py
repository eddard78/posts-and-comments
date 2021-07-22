from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsPostOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class IsCommentOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return obj.author == request.user or obj.post.author == request.user
        return obj.author == request.user