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
    def __init__(self, name="", breed=""):
        self._name = name
        self._breed = breed

    def get_name(self):
        print("Retrieving Dog Name")
        return self._name

    def set_name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            return "Name must be string between 1 and 25 characters."
        else:
            self._name = name
            
    name = property(get_name, set_name)

    def get_breed(self):
        print("Retrieving breed")
        return self._breed

    def set_breed(self, breed):
        if breed not in APPROVED_BREEDS:
            return "Breed must be in list of approved breeds."
        else:
            self._breed = breed

    breed = property(get_breed, set_breed)