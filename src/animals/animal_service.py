from animals.animal_repositories import AnimalRepository
from enum import Enum

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"

class AnimalService:
    def __init__(self, repository: AnimalRepository):
        self.repository = repository

    def validate_animal(self, animal):
        species = animal.get("species")
        age = animal.get("age")
        special_requirements = animal.get("special_requirements")
        gender = animal.get("gender")

        if not species or not isinstance(species, str) or not (5 <= len(species) <= 100):
            raise ValueError("Animal species must be a string between 5 and 100 characters")

        # if not age or not isinstance(age, int) or age < 0:
        #     raise ValueError("Animal age must be a non-negative integer")

        # if not special_requirements or not isinstance(special_requirements, str):
        #     raise ValueError("Animal special requirements must be a string")
        
        if gender not in [g.value for g in Gender]:
            raise ValueError("Animal gender must be one of: 'male' or 'female'")

    def create_animal(self, animal):
        self.validate_animal(animal)
        return self.repository.save_animal(animal)

    def get_animal(self, id):
        return self.repository.get_animal(int(id))

    def delete_animal(self, id):
        return self.repository.delete_animal(int(id))
    
    def get_all_animal(self):
        return self.repository.get_all_animal()

    def get_animal_by_gender(self, gender):
        if gender not in [g.value for g in Gender]:
            raise ValueError("Invalid gender")
        return self.repository.get_animal_by_gender(gender)
