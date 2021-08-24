import pytest
import json

from model_bakery import baker

from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.mark.django_db(transaction=False)
class TestUserEndpoints:

    def test_list(self):
        baker.make(User, _quantity=3)

        api_client = APIClient()

        response = api_client.get('/users/')

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3
