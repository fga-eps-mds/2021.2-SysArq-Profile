from rest_framework import viewsets
from rest_framework import mixins
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny


class CreateUserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
