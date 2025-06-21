#Create classes Dog, Cat, and Bird, each with a method make_sound().
#Implement different behaviors for make_sound() in each class.
#Create a function let_them_speak() that takes a list of objects and calls their make_sound() method polymorphically.

class Dog:
    def make_sound(self):
        print("Wooof....")

class Duck:
    def make_sound(self):
        print("Quacks....")
        
class Bird:
    def make_sound(self):
        print("chirps....")
        
def let_them_speak():
    speaks =[Dog(), Duck(), Bird()]
    
    for speak in speaks:
        speak.make_sound()

let_them_speak()