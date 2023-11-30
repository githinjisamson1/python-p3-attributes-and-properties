#!/usr/bin/env python3

APPROVEDnameS = [
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

    def __init__(self):
        self._name = "Snoopy"
        self._breed = "Mastiff"

    def get_name(self):
        print("Retrieving name...")
        return self._name

    def set_name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")

        else:
            print(f"Setting name to {name}")
            self._name = name

    def get_breed(self):
        print("Retrieving breed...")
        return self._breed

    def set_breed(self, breed):
        if breed not in APPROVEDnameS:
            print("Breed must be in list of approved breeds.")
        else:
            return self._breed

    name = property(get_name, set_name)

    breed = property(get_breed, set_breed)


fido = Dog()
print(fido.name)
print(fido.breed)
# fido.name = "New name"
