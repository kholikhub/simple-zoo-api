class AnimalRepository:
    def __init__(self):
        self.animal = {}
        self.id = 1

    def get_all_animal(self):
        return list(self.animal.values())

    def save_animal(self, animal):
        animal["id"] = self.id
        self.animal[self.id] = animal
        self.id += 1
        return animal

    def get_animal(self, id):
        print(self.animal)
        return self.animal.get(id)

    def delete_animal(self, id):
        print(id)
        return self.animal.pop(id, None)

    def get_animal_by_gender(self, gender):
        return [animal for animal in self.animal.values() if animal["gender"] == gender]
