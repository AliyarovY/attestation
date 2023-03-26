from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAdminUser
)
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer
from base.permissions import IsSelf


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action in ('retrieve', 'list'):
            permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.action in ('update', 'partial_update'):
            permission_classes = [IsAdminUser, IsSelf]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
