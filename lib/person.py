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
    def __init__(self):
        self._name = "John"
        self._job = None
        
    def get_name(self):
        return self._name

    def set_name(self, name):
        if (isinstance(name, str)) and (len(name) <= 25):
            self._name = name
        else:
            print("Name must be string under 25 characters.")

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self._job = job
            
    name = property(get_name, set_name)
    job = property(get_job, set_job)


person1 = Person()
print(person1.name)
# person1.job="developer"
# print(person1.job)
# getattr(person1, "_job")
