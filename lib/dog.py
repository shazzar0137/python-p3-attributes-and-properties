#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Unknown", breed="Pug"):  #
        self.name = name        
        self.breed = breed

    #@property
    def get_name(self):
        return self._name

    #@name.setter
    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    #@property
    def get_breed(self):
        return self._breed

    #@breed.setter
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
    pass


snopy =Dog("andrew","Pug")
print(snopy.name)
snopy.name = "gggjfjggjfsgjjgsgjgsggjkhsjyugfsurygksygsgylseygriurliuhgeilsuglsgslieugrluiselrgls"
print(snopy.name)
snopy.name = "1"
print(snopy.name)
print(snopy.breed)
snopy.breed = "Damascus"
print(snopy.breed)
