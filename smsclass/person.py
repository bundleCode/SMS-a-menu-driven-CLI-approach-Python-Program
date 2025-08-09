# ---------------- Person Class ----------------

class Person:
    # Constructor
    def __init__(self, name, age, address):
        if not isinstance(age, int):
            raise TypeError("Student Age must be an integer")
        if age < 10:
            raise TypeError("Student Age can't be less than 10")
        if name.isdigit():
            raise TypeError("Student Name can't be all digits.")
        if len(name) < 2:
            raise TypeError("Very short name is given.")

        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        return {
            "name": self.name,
            "age": self.age,
            "address": self.address
        }
