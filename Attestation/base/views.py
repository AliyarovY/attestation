from rest_framework.decorators import action
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAdminUser
)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAuthor


class CommentPostViewMixin(ModelViewSet):
    """ Mixin for Post and Comment ViewSets"""

    def get_permissions(self):
        permission_classes = []
        valid_action_permissions = {
            ('create', 'my'): [IsAuthenticated],
            ('update', 'partial_update', 'delete'): [IsAdminUser, IsAuthor],
            ('list', 'retrieve'): [AllowAny],
        }
        for actions, perm in valid_action_permissions.items():
            if self.action in actions:
                permission_classes = perm
        if not permission_classes:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(methods=['get'], detail=False)
    def my(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(author=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
