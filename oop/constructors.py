class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person(name = "Cathrine", age = 24)

print(f"My name is {person1.name}, I am {person1.age} years old!")