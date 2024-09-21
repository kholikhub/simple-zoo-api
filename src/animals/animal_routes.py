from flask import Blueprint, request, jsonify
from animals.animal_repositories import AnimalRepository
from animals.animal_service import AnimalService
from flasgger import swag_from
import os

animal_routes = Blueprint("animal_routes", __name__)

repository = AnimalRepository()
service = AnimalService(repository=repository)

@animal_routes.route("/animals", methods=["POST"])
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/add_animal.yml'))
def create_animal():
    animal = request.get_json()
    try:
        animal = service.create_animal(animal)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify(animal), 200

@animal_routes.route("/animals/<int:id>", methods=["GET"])
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/get_animal.yml'))
def get_animal(id):
    animal = service.get_animal(id)
    if animal is None:
        return jsonify({"error": "Animal not found"}), 404
    return jsonify(animal)

@animal_routes.route("/animals/<int:id>", methods=["DELETE"])
@swag_from(
    {
        "tags": ["Animals"],
        "parameters": [
            {
                "in": "path",
                "name": "id",
                "schema": {"type": "integer"},
                "required": True,
                "description": "The animal ID",
            }
        ],
        "responses": {
            204: {"description": "Animal deleted"},
            404: {"description": "Animal not found"},
        },
    }
)
def delete_animal(id):
    animal = service.delete_animal(id)
    if animal is None:
        return jsonify({"error": "Animal not found"}), 404
    return "", 204

@animal_routes.route("/animals", methods=["GET"])
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/get_all_animal.yml'))
def get_all_animal():
    animals = service.get_all_animal()
    return jsonify(animals)

@animal_routes.route("/animals/gender/<string:gender>", methods=["GET"])
@swag_from(os.path.join(os.path.dirname(__file__), 'docs/get_animal_by_gender.yml'))
def get_animal_by_gender(gender):
    try:
        animals = service.get_animal_by_gender(gender)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    return jsonify(animals)
