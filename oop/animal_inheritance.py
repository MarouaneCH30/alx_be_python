class Animal:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        
    def eat(self):
        print(f"{self.name} eats meat")
        
    def sleep(self):
        print(f"{self.name} sleeps every night")

class Dog(Animal):
    
    def __init__(self, name, age):
        super().__init__(name, age)
        
    
    def bark(self):
        print(f"{self.name} barks!")
        

dog1 = Dog('Bobby', 5, )
dog1.sleep()

dog1.bark()

