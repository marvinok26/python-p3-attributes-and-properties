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

    @property
    def name(self):
        print("Retrieving Dog Name")
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be a string between 1 and 25 characters.")
        else:
            print(f"The dog name is {name}")
            self._name = name

    @property
    def breed(self):
        print("Retrieving breed")
        return self._breed

    @breed.setter
    def breed(self, breed):
        if breed not in APPROVED_BREEDS:
            print("Breed must be in the list of approved breeds.")
        else:
            print(f"The dog breed is {breed}")
            self._breed = breed