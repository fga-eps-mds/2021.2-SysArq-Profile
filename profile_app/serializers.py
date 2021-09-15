from .models import User
from rest_framework import serializers


class CreateUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'cpf', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, data):
        password = data.pop('password', None)
        obj = self.Meta.model(**data)
        if password is not None:
            obj.set_password(password)
        obj.save()
        return obj


class GetUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']
