import pytest
from rest_framework.test import APIClient
from dotenv import load_dotenv
import os


@pytest.mark.django_db(transaction=False)
class TestUserEndpoints:

    def test_create(self):
        load_dotenv()
        data = {
            "username": "test",
            "first_name": "test",
            "last_name": "test",
            "cpf": "11111111111",
            "password": os.getenv('POSTGRES_HOST')
        }

        api_client = APIClient()
        response = api_client.post(
            '/users/register/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201
