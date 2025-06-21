class Robot:
    
    #defining a constructor
    
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
         
    
    #This is a method of the class
    def introduce_self(self):
        print(f"My name is { self.name}, I weigh {self.weight} \nMy favorite color is {self.color}" )


r1 = Robot("Gucha","Red", 20)
r2 = Robot("Jerry","Blue", 30)
r1.introduce_self()
r2.introduce_self()


class Person:
    def __init__(person, name, personality, gender):
        person.name = name
        person.personality = personality
        person.gender = gender
        
    def intro(person):
    
     print(f"My name is {person.name}, My personality is {person.personality}. My gender is {person.gender}") 
 

person1 = Person('Gucha', 'Sijui bro', 'Male')

person1.intro()

    
        



