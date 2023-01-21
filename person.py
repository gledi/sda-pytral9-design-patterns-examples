"""
A module to work with people
"""

class Person:
    """A class that represents a person"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_full_name(self):
        """Get a person's fullname"""
        return f'{self.name} {self.surname}'

    @classmethod
    def create_person(cls, fullname):
        """create a person from fullname"""
        name, surname = fullname.split()
        return cls(name, surname)
