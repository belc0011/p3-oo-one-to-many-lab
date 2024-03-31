class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner="default"):
        found_match = False
        self.name = name
        for pet in Pet.PET_TYPES:
            print(pet)
            if pet == pet_type:
                self.pet_type = pet_type
                found_match = True
        if (not found_match):
            raise Exception("pet must be of approved type")
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        pet_list = []
        for pet in Pet.all:
            if pet.owner == self:
                pet_list.append(pet)
        return pet_list
    
    def add_pet(self, pet):
        if (isinstance(pet, Pet)):
            pet.owner = self
        else:
            raise Exception("pet must be of class Pet")
    
    def get_sorted_pets(self):
        pet_list = self.pets()
        return sorted(pet_list, key=lambda pet: pet.name)
