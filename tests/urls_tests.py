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


    def test_get_user(self):
        USERNAME = "test"
        PASSWORD = "test"
        
        data = {
            "username": USERNAME,
            "first_name": "test",
            "last_name": "test",
            "password": PASSWORD 
        }

        api_client = APIClient()
        user_response = api_client.post(
            "/users/register/", 
            data=data,
            header={"Content-Type": "application/json"},
            format='json'
        )

        user_token = api_client.post(
            "/api/token/",
            data = {
                "username": USERNAME,
                "password": PASSWORD
            },
            header={"Content-Type": "application/json"},
            format="json"
        )
