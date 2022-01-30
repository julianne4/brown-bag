#Create animal classes with instance methods

class Dog:
    """A dog with a name and an age"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says woof!"
