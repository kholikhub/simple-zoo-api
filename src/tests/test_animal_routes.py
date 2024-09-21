import pytest
from flask import json, Flask
from unittest.mock import MagicMock

from app import app
from animals.animal_routes import animal_routes


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_create_animal(client):
    animal_routes.service = MagicMock()
    animal = {"id": 1, "species": "Lion", "age": 3, "special_requirements": "None", "gender": "male"}
    animal_routes.service.create_animal.return_value = animal

    response = client.post(
        "/animals", data=json.dumps(animal), content_type="application/json"
    )

    animal_routes.service.create_animal.assert_called_once_with(animal)
    assert response.status_code == 200
    assert json.loads(response.get_data()) == animal


def test_get_animal(client):
    animal_routes.service = MagicMock()
    animal = {"id": 1, "species": "Lion", "age": 3, "special_requirements": "None", "gender": "male"}
    animal_routes.service.get_animal.return_value = animal

    response = client.get("/animals/1")

    animal_routes.service.get_animal.assert_called_once_with(1)
    assert response.status_code == 200
    assert json.loads(response.get_data()) == animal


def test_delete_animal(client):
    animal_routes.service = MagicMock()
    animal_routes.service.delete_animal.return_value = None

    response = client.delete("/animals/1")

    animal_routes.service.delete_animal.assert_called_once_with(1)
    assert response.status_code == 204
