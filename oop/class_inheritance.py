class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print("Generic Animal Sound")
        
#inheritance of Animal class

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        
        self.breed = breed
    
    def make_sound(self):
        print("Woof!")
    
    
dog = Dog('Bobby', 'Labrador')
dog.make_sound()