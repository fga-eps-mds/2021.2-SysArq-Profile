from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from .models import User
from .serializers import CreateUserSerializer, GetUserSerializer, UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


class CreateUserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class GetUsersViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = GetUserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
