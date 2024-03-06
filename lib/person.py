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

    def get_name(self):
        print("Retrieving Person Name")
        return self._name

    def set_name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            return "Name must be string between 1 and 25 characters."
        else:
            self._name = name.title()

    name = property(get_name, set_name)

    def get_job(self):
        print("Retrieving job")
        return self._job

    def set_job(self, job):
        if job not in APPROVED_JOBS:
            return "Job must be in list of approved jobs."
        else:
            self._job = job

    job = property(get_job, set_job)

   


    

    
