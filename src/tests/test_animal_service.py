from unittest.mock import MagicMock

import pytest
from animals.animal_service import AnimalService, Gender


@pytest.fixture
def service():
    repository = MagicMock()
    return AnimalService(repository)


@pytest.mark.parametrize(
    "animal, expected_exception",
    [
        (
            {
                "species": "Dog",
                "age": -1,
                "special_requirements": "None",
                "gender": "male",
            },
            ValueError,
        ),
        (
            {
                "species": "C",
                "age": 3,
                "special_requirements": "None",
                "gender": "male",
            },
            ValueError,
        ),
        (
            {
                "species": "Dog",
                "age": 3,
                "special_requirements": "",
                "gender": "male",
            },
            ValueError,
        ),
        (
            {
                "species": "Dog",
                "age": 3,
                "special_requirements": "None",
                "gender": "invalid",
            },
            ValueError,
        ),
    ],
)
def test_validate_animal(service, animal, expected_exception):
    with pytest.raises(expected_exception):
        service.validate_animal(animal)


def test_create_animal(service):
    animal = {
        "species": "Lion",
        "age": 3,
        "special_requirements": "None",
        "gender": "male",
    }
    service.repository.save_animal.return_value = animal

    result = service.create_animal(animal)

    service.repository.save_animal.assert_called_once_with(animal)
    assert result == animal


def test_get_animal(service):
    animal = {
        "species": "Lion",
        "age": 3,
        "special_requirements": "None",
        "gender": "male",
    }
    service.repository.get_animal.return_value = animal

    result = service.get_animal(1)

    service.repository.get_animal.assert_called_once_with(1)
    assert result == animal


def test_delete_animal(service):
    service.repository.delete_animal.return_value = None

    result = service.delete_animal(1)

    service.repository.delete_animal.assert_called_once_with(1)
    assert result is None


@pytest.mark.parametrize(
    "gender, expected_animals",
    [
        (
            "male",
            [
                {
                    "species": "Lion",
                    "age": 3,
                    "special_requirements": "None",
                    "gender": "male",
                }
            ],
        ),
        ("female", []),
    ],
)
def test_get_animal_by_gender(service, gender, expected_animals):
    service.repository.get_animal_by_gender.return_value = expected_animals

    result = service.get_animal_by_gender(gender)

    service.repository.get_animal_by_gender.assert_called_once_with(gender)
    assert result == expected_animals
