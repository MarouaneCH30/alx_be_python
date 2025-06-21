#Create two parent classes Bird and Mammal with methods fly() and run(),
#Create a subclass Bat that inherits from both Bird and Mammal and implements fly() and run() methods

class Bird:
    def fly(self):
        print("Flying....")

class Mammal:
    def run(self):
        print("Running......")

class Bat(Bird, Mammal):
    pass

bat = Bat()
bat.fly()
bat.run()