#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="", job=""):
        self._name = name
        self._job = job

    @property
    def name(self):
        print("Retrieving Person Name")
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be a string between 1 and 25 characters.")
        else:
            print(f"The person's name is {name}")
            self._name = name.title()

    @property
    def job(self):
        print("Retrieving job")
        return self._job

    @job.setter
    def job(self, job):
        if job not in APPROVED_JOBS:
            print("Job must be in the list of approved jobs.")
        else:
            print(f"The person's job is {job}")
            self._job = job