#!/usr/bin/python3
"""3232"""


import pickle


class CustomObject:
    """3434"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"""
Name: {self.name}
Age: {self.age}
Is Student: {self.is_student}
""")

    def serialize(self, filename):
        with open(filename, "wb") as mf:
            pickle.dump(self, mf)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as mf:
                return pickle.load(mf)
        except Exception:
            return None
