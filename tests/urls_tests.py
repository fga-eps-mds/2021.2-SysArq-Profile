import pytest
from rest_framework.test import APIClient
from dotenv import load_dotenv
from profile_app.models import User
import os


@pytest.mark.django_db(transaction=False)
class TestUserEndpoints:

    @pytest.fixture
    def api_client(self):
        admin_username = os.getenv('FIRST_USERNAME')
        admin_password = os.getenv('FIRST_PASSWORD')
        api_client = APIClient()

        admin_token = api_client.post(
            '/api/token/',
            data={
                'username': admin_username,
                'password': admin_password
            },
            format="json"
        )
        api_client.credentials(HTTP_AUTHORIZATION='JWT ' + admin_token.data["access"])
        return api_client

    def test_create(self, api_client):
        load_dotenv()
        data = {
            "username": "test",
            "user_type": "VI",
            "first_name": "test",
            "last_name": "test",
            "cpf": "11111111111",
            "password": os.getenv('POSTGRES_HOST')
        }

        response = api_client.post(
            '/users/register/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    def test_create_superuser(self, api_client):
        response = api_client.post(
            '/users/register/',
            data={
                'username': 'superuser',
                'user_type': "AD",
                'password': 'superuser',
                'cpf': '00000000000',
                'is_superuser': 'true'
            },
            format='json'
        )
        assert response.status_code == 201

    def test_get_user(self, api_client):
        USERNAME = "test"
        PASSWORD = "test"

        data = {
            "username": USERNAME,
            "user_type": "AD",
            "first_name": "test",
            "last_name": "test",
            "password": PASSWORD
        }

        user_response = api_client.post(
            "/users/register/",
            data=data,
            header={"Content-Type": "application/json"},
            format='json'
        )

        assert user_response.status_code == 201

        token_response = api_client.post(
            "/api/token/",
            data={
                "username": USERNAME,
                "password": PASSWORD
            },
            format="json"
        )

        api_client.credentials(HTTP_AUTHORIZATION='JWT ' + token_response.data["access"])

        users_response = api_client.get(
            "/users/get-users/",
            format="json",
        )

        assert users_response.status_code == 200
        assert users_response.data[-1]["first_name"] == "test"


@pytest.mark.django_db()
class TestDatabaseAccess:

    def test_create_superuser(self):
        new_user = User.objects.create_superuser(
            username='super',
            user_type=User.User_Type.AD,
            password='super',
            first_name='super',
            last_name='super',
            cpf='00000000000')
        assert new_user.username == 'super'

        with pytest.raises(ValueError):
            # This fails since is_superuser cannot be false in create_superuser
            User.objects.create_superuser(username='super2',
                                          user_type=User.User_Type.AD,
                                          password='super2',
                                          first_name='super2',
                                          last_name='super2',
                                          cpf='00000000000',
                                          is_superuser=False)
