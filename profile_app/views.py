from rest_framework import viewsets
from rest_framework import mixins
from .models import User
from .serializers import CreateUserSerializer, GetUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


class CreateUserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class GetUsersViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = GetUserSerializer
